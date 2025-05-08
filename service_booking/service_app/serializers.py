# # service_app/serializers.py
# from rest_framework import serializers
# from .models import User, Service, Booking
# from rest_framework_simplejwt.tokens import RefreshToken

# # User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

# # Service Serializer
# class ServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = ['id', 'name', 'description', 'price', 'available_slots']

# # Booking Serializer
# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = ['user', 'service', 'status', 'booking_date']
