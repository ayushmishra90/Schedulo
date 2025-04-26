from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Service, Booking
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

@login_required
def services_page(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    booking = Booking.objects.create(user=request.user, service=service, status='Pending')
    return render(request, 'booking_success.html', {'booking': booking})
