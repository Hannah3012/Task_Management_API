from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = ["id", "title", "description", "owner", "status", "due_date", "created_at", "updated_at"]
        read_only_fields = ["id", "owner", "created_at", "updated_at"]
