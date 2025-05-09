from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Service, Booking
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, BookingForm, ServiceForm
from django.http import HttpResponseForbidden
from datetime import datetime
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from django.utils.html import escape
from django.urls import reverse
@never_cache
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    return render(request, 'home.html')
@never_cache
def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})




@never_cache
@login_required
def book_service(request, service_id):
    # Retrieve the service object with the given service_id
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        # Get the selected date from the form
        selected_date_str = request.POST.get('date')
        if not selected_date_str:
            return render(request, 'book_service.html', {
                'service': service,
                'error': 'Please select a valid date.',
            })

        try:
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()
        except ValueError:
            return render(request, 'book_service.html', {
                'service': service,
                'error': 'Invalid date format. Please select a valid date.',
            })
        existing_booking = Booking.objects.filter(service=service, date=selected_date).first()
        if existing_booking:
            return render(request, 'book_service.html', {
                'service': service,
                'error': 'This service has already been booked for the selected date. Please choose another date.',
            })
        # When confirming the booking
        if 'confirm' in request.POST:
            booking = Booking.objects.create(
                customer=request.user,
                service=service,  # Ensure that the service is passed correctly
                date=selected_date,
                status='Pending'
            )
            # return render(request, 'booking_success.html', {'booking': booking})
            return redirect('booking_success', booking_id=booking.id)

        else:
            form = BookingForm(initial={'date': selected_date})
            return render(request, 'book_service.html', {
                'form': form,
                'service': service,
                'selected_date': selected_date
            })

    return render(request, 'book_service.html', {'service': service})


# @login_required
# def book_service(request, service_id):
#     service = get_object_or_404(Service, id=service_id)

#     if request.method == 'POST':
#         # Get the selected date from the form
#         selected_date_str = request.POST.get('date')
#         if selected_date_str:
#             selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()

#         # Create form instance with the selected service
#         form = BookingForm(request.POST)

#         if form.is_valid():
#             # If form is valid, save the booking
#             booking = form.save(commit=False)
#             booking.customer = request.user
#             booking.service = service
#             booking.status = 'Pending'
#             booking.date = selected_date  # Set the selected date

#             booking.save()

#             # Redirect to success page after booking
#             return render(request, 'booking_success.html', {'booking': booking})

#     else:
#         form = BookingForm(service=service)

#     return render(request, 'book_service.html', {'form': form, 'service': service})


@never_cache
@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            # Add more fields here as needed for uniqueness

            # Check if service already exists for this user
            existing = Service.objects.filter(
                name=name,
                description=description,
                owner=request.user
            ).exists()

            if existing:
                return render(request, 'add_service.html', {
                    'form': form,
                    'error': 'This service already exists.'
                })

            service = form.save(commit=False)
            service.owner = request.user
            service.save()
            return HttpResponse(f'<script>location.replace("{escape(reverse("services"))}");</script>')
    else:
        form = ServiceForm()

    return render(request, 'add_service.html', {'form': form})

# def add_service(request):
#     if request.method == 'POST':
#         form = ServiceForm(request.POST)
#         if form.is_valid():
#             service = form.save(commit=False)
#             service.owner = request.user
#             service.save()
#             return redirect('services')
#     else:
#         form = ServiceForm()
#     return render(request, 'add_service.html', {'form': form})

@never_cache
@login_required
def manage_bookings(request, service_id):
    service = get_object_or_404(Service, id=service_id, owner=request.user)
    bookings = Booking.objects.filter(service=service).order_by('-date')
    return render(request, 'manage_bookings.html', {'service': service, 'bookings': bookings})

@never_cache
@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(service__owner=request.user).order_by('-created_at')
    return render(request, 'view_bookings.html', {'bookings': bookings})


@never_cache
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'my_bookings.html', {'bookings': bookings})

@never_cache
@login_required
def cancel_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, customer=request.user)
    except Booking.DoesNotExist:
        return redirect('services')  # Redirect if user goes back after deletion

    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')

    return render(request, 'confirm_cancel.html', {'booking': booking})

@never_cache
@login_required
def update_booking_status(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return HttpResponse(f'<script>location.replace("{escape(reverse("view_bookings"))}");</script>')

    if not booking.can_change_status(request.user):
        return HttpResponseForbidden("You are not authorized to change this booking status.")

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Booking.STATUS_CHOICES):
            booking.status = new_status
            booking.save()
            return HttpResponse(f'<script>location.replace("{escape(reverse("view_bookings"))}");</script>')

    return render(request, 'update_booking_status.html', {
        'booking': booking,
        'status_choices': Booking.STATUS_CHOICES
    })

# def update_booking_status(request, booking_id):
#     try:
#         booking = Booking.objects.get(id=booking_id)
#     except Booking.DoesNotExist:
#         return redirect('services')

#     if not booking.can_change_status(request.user):
#         return HttpResponseForbidden("You are not authorized to change this booking status.")

#     if request.method == 'POST':
#         new_status = request.POST.get('status')
#         if new_status in dict(Booking.STATUS_CHOICES):
#             booking.status = new_status
#             booking.save()
#             return redirect('view_bookings')
            

#     return render(request, 'update_booking_status.html', {
#         'booking': booking,
#         'status_choices': Booking.STATUS_CHOICES
#     })

@never_cache
@login_required
def my_services(request):
    services = Service.objects.filter(owner=request.user)
    return render(request, 'my_services.html', {'services': services})

@never_cache
@login_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, owner=request.user)
    service.delete()
    return redirect('my_services')

@never_cache
@login_required
def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_success.html', {'booking': booking})
