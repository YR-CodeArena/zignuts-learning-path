from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

# Serializer for registering new users
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Using create_user ensures the password gets properly hashed
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    # Make owner read-only so users can't fake or assign tasks to other people
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'owner']
