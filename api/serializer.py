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