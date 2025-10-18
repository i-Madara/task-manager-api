from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.utils.timezone import now
from datetime import timedelta

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="p1")
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_and_list_task(self):
        payload = {
            "title": "Test Task",
            "description": "D1",
            "deadline": (now() + timedelta(days=2)).isoformat(),
            "completed": False
        }
        r = self.client.post("/api/tasks/", payload, format="json")
        self.assertEqual(r.status_code, 201)
        r = self.client.get("/api/tasks/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["count"], 1)
