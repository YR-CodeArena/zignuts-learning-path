from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


# Serializer for registering a new user
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # create_user automatically hashes the password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


# Serializer for Task objects
class TaskSerializer(serializers.ModelSerializer):
    # Display the owner username as plain text (read-only)
    owner = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'owner']
