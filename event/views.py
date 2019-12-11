from .models import Event, Session
from .serializers import EventSerializer, SessionSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

# Views for End-Points.

# View for Event/s
class EventView(viewsets.ModelViewSet):
    """
    API endpoint that allows the list of events to be viewed.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["start_date"] > serializer.validated_data["end_date"]:
                return Response({"Failed": "Start Date must be before End Date!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=id):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["start_date"] > serializer.validated_data["end_date"]:
                return Response({"Failed": "Start Date must be before End Date!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
# View for Session/s
class SessionView(viewsets.ModelViewSet):
    """
    API endpoint that allows the list of sessions to be viewed.
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def create(self, request):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["start_date"] > serializer.validated_data["end_date"]:
                return Response({"Failed": "Start Date must be before End Date!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def update(self, request, pk=id):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["start_date"] > serializer.validated_data["end_date"]:
                return Response({"Failed": "Start Date must be before End Date!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  