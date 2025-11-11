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
    move_in_date = serializers.DateField(required=True)
    move_out_date = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = Tenants
        fields = [
            'id', 'name', 'email', 'contact_number', 'pg', 'room',
            'move_in_date', 'move_out_date', 'is_active', 'rent'
        ]
