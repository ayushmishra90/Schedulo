from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Booking,Service

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['date'].required = True

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['owner']
        fields = ['name', 'description', 'price', 'duration']
        
class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']
