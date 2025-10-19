from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ('id','owner','title','description','due_date','priority','status','completed_at','created_at','updated_at')
        read_only_fields = ('completed_at','created_at','updated_at')

    def validate_due_date(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError('Due date must be in the future.')
        return value

    def validate_priority(self, value):
        valid = [c[0] for c in Task.PRIORITY_CHOICES]
        if value not in valid:
            raise serializers.ValidationError('Invalid priority.')
        return value

    def validate(self, data):
        instance = getattr(self, 'instance', None)
        if instance and instance.status == 'completed':
            new_status = data.get('status', instance.status)
            if new_status != 'pending':
                raise serializers.ValidationError('Completed tasks cannot be edited unless reverted to pending.')
        return data