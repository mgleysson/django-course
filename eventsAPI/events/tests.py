import unittest

from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase

from events.models import Event, Comment, Tag


class EventsTestCase(TestCase):

    def setUp(self):
        Event.objects.create(event="Teste 1", date="2020-10-09T10:00:00+03:00", priority="2")
        Event.objects.create(event="Teste 2", date="2020-10-10 14:00:00", priority="3")
        e = Event.objects.create(event="Teste 3", date="2020-10-10 14:00:00", priority="3")
        Comment.objects.create(author="Marcos", email="mgsn@test.com", text="Teste comentário",
                                   date="2020-10-12T10:00:00+03:00", event=e)
        Tag.objects.create(title='DjangoCourse', information='Info')

    def test_text_priority(self):
        event = Event.objects.get(event="Teste 1")
        self.assertEquals(event.text_priority, "Urgente")

    def test_text_priority_invalid(self):
        event = Event.objects.create(event="Teste 3", date="2020-10-09", priority="4")
        self.assertEquals(event.text_priority, "")

    @unittest.expectedFailure
    def test_date(self):
        Event.objects.create(event="Teste 4", date="09-10-2020", priority="1")

    def test_str_event(self):
        event = Event.objects.get(event="Teste 1")
        self.assertEquals(str(event), "Teste 1 - 2020-10-09 07:00:00+00:00")

    def test_str_comment(self):
        comment = Comment.objects.get(text="Teste comentário")
        self.assertEquals(str(comment), "Marcos - 2020-10-12 07:00:00+00:00")

    def test_str_tag(self):
        tag = Tag.objects.get(title="DjangoCourse")
        self.assertEquals(str(tag), "DjangoCourse")


class EventViewTests(APITestCase):

    def setUp(self):
        e = Event.objects.create(event="Teste 5", date="2020-10-09", priority="1")
        Comment.objects.create(author="Marcos", email="mgsn@test.com", text="Teste comentário",
                               date="2020-10-12T10:00:00+03:00", event=e)
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

    def test_post_bad_request(self):
        response = self.client.post("/api/v1/events/", {'eventChanged': 'Teste 6', 'date': '2020-10-11T10:00:00', 'priority': '0'})
        self.assertEquals(response.status_code, 400)
        response2 = self.client.get("/api/v1/events/")
        self.assertEquals(len(response2.data['results']), 1)

    def test_get_comment(self):
        response = self.client.get("/api/v1/comments/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data['results']), 1)
        self.assertEquals(response.data['results'][0]['text'], 'Teste comentário')

    def test_delete_event_comments_cascade(self):
        e = Event.objects.get(event='Teste 5')
        response = self.client.delete('/api/v1/events/' + str(e.id) + '/')
        self.assertEquals(response.status_code, 204)
        response2 = self.client.get("/api/v1/events/")
        self.assertEquals(len(response2.data['results']), 0)
        response3 = self.client.get('/api/v1/comments/')
        self.assertEquals(len(response3.data['results']), 0)
