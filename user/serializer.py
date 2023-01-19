from rest_framework import serializers
from user.models import User, Event
from user.validators import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'birth_date', 'password', 'created_at', 'updated_at']

    def validate(self, data):
        if not validate_name(data['name']):
            raise serializers.ValidationError({'name': 'O nome deve conter somente letras.'})
        return data


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ListEventsByUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
