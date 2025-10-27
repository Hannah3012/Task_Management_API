from rest_framework import serializers
from .models import Task, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "task", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "created_at", "updated_at"]

class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "status", "due_date", 
            "author", "comments", "created_at", "updated_at"
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at"]
