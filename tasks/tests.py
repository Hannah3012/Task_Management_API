from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Task
from django.utils import timezone
from datetime import timedelta

class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('u1','u1@example.com','pass')
        self.client.login(username='u1', password='pass')

    def test_create_task_future_due(self):
        url = reverse('task-list')
        data = {
            'title':'t1',
            'description':'d',
            'due_date':(timezone.now()+timedelta(days=2)).isoformat(),
            'priority':'low'
        }
        r = self.client.post(url, data, format='json')
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
