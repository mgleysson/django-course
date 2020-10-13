import unittest

from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase

from events.models import Event


class EventsTestCase(TestCase):

    def setUp(self):
        Event.objects.create(event="Teste 1", date="2020-10-09T10:00:00+03:00", priority="2")
        Event.objects.create(event="Teste 2", date="2020-10-10 14:00:00", priority="3")

    def test_text_priority(self):
        event = Event.objects.get(event="Teste 1")
        self.assertEquals(event.text_priority, "Urgente")

    def test_text_priority_invalid(self):
        event = Event.objects.create(event="Teste 3", date="2020-10-09", priority="4")
        self.assertEquals(event.text_priority, "")

    @unittest.expectedFailure
    def test_date(self):
        Event.objects.create(event="Teste 4", date="09-10-2020", priority="1")


class EventViewTests(APITestCase):

    def setUp(self):
        Event.objects.create(event="Teste 5", date="2020-10-09", priority="1")
        User.objects.create_user(username='test', password='test')
        response = self.client.post("/api-auth-token", {'username': 'test', 'password': 'test'})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_get(self):
        response = self.client.get("/api/v1/events/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data['results']), 1)
        self.assertEquals(response.data['results'][0]['event'], 'Teste 5')

    def test_post(self):
        response = self.client.post("/api/v1/events/", {'event': 'Teste 6', 'date': '2020-10-11T10:00:00', 'priority': '0'})
        self.assertEquals(response.status_code, 201)
        response2 = self.client.get("/api/v1/events/")
        self.assertEquals(len(response2.data['results']), 2)
