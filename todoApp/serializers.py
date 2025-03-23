from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task', 'user', 'state', 'priority', 'created_at', 'ends_at')
        read_only_fields = ('created_at',)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'key')
        