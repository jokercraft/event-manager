from .models import Event, Session
from rest_framework import serializers

# Serializers for Event and Session models.
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'name', 'start_date', 'end_date', 'timezone', 'sessions']

class SessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Session
        fields = ['id', 'name', 'start_date', 'end_date', 'speaker']
