from rest_framework import serializers
from api.models import *

class PgsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pgs
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenants
        fields = ['id', 'name', 'email', 'contact_number', 'pg', 'room', 'is_active']