from rest_framework import serializers
from .models import Booking, MenuItem
from django.contrib.auth.models import User

# Converts User instances to and from JSON format, making them usable in API endpoints
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # url in fields links to user instance with HyperlinkedModelSerializer
        fields = ['url', 'username', 'email', 'groups']
        

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'