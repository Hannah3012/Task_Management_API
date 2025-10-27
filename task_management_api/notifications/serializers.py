from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source="actor.username")
    target_str = serializers.ReadOnlyField(source="target.__str__")

    class Meta:
        model = Notification
        fields = ["id", "actor_username", "verb", "target_str", "read", "timestamp"]
