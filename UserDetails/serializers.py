from rest_framework import serializers
from .models import User_details, User_Address

class User_Address_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Address
        fields = ['id', 'city', 'state', 'country']

class User_Detail_Serializer(serializers.ModelSerializer):
    addresses = User_Address_Serializer(many=True)  # Nested serializer for addresses

    class Meta:
        model = User_details
        fields = ['id', 'name', 'phone_number', 'email', 'addresses']
