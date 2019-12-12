from django.test import TestCase, Client
from rest_framework.test import APITestCase
from .models import Event, Session
from rest_framework import status
from .serializers import EventSerializer
from rest_framework.response import Response


client = Client()

# Tests for Models are here.
class EventTest(TestCase):
    """ Test module for Event model """

    def setUp(self):
        Event.objects.create(
            name='Casper', start_date="2020-01-02", end_date="2020-01-02", timezone='EU')

    def test_puppy_breed(self):
        event_casper = Event.objects.get(name='Casper')
        self.assertEqual(
            event_casper.timezone, "EU")


# Tests for API End-Points are here.
class GetAllEventsTest(TestCase):
    """ Test module for GET all events API """

    def test_get_all_events(self):
        # get data from db
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        self.assertEqual([], serializer.data)
        self.assertEqual(Response.status_code, status.HTTP_200_OK)
