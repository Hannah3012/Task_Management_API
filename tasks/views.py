from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.utils import timezone
from rest_framework.permissions import AllowAny

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from .permissions import IsOwner
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'status': ['exact'],
        'priority': ['exact'],
        'due_date': ['lte','gte','exact'],
    }
    ordering_fields = ['due_date','priority']

    def get_queryset(self):
        # each user only sees their own tasks
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        # If status switched to completed, set completed_at
        new_status = self.request.data.get('status')
        instance = getattr(self, 'get_object')()
        # serializer.save will run serializer.validate
        saved = serializer.save()
        return saved

    @action(detail=True, methods=['post'], url_path='mark', url_name='mark')
    def mark(self, request, pk=None):
        """Custom endpoint to mark complete/incomplete: POST /tasks/{id}/mark/ with {"status":"completed"} or {"status":"pending"}
        """
        task = self.get_object()
        status_val = request.data.get('status')
        if status_val not in dict(Task.STATUS_CHOICES).keys():
            return Response({'detail':'Invalid status.'}, status=status.HTTP_400_BAD_REQUEST)

        if status_val == 'completed' and task.status != 'completed':
            task.status = 'completed'
            task.completed_at = timezone.now()
            task.save()
            serializer = self.get_serializer(task)
            return Response(serializer.data)

        if status_val == 'pending' and task.status == 'completed':
            task.status = 'pending'
            task.completed_at = None
            task.save()
            serializer = self.get_serializer(task)
            return Response(serializer.data)

        return Response({'detail':'No change performed.'}, status=status.HTTP_200_OK)