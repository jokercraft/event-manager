from rest_framework import status
from .models import Event, Session
from .serializers import EventSerializer, SessionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Views for End-Points.

# To get an event by 'id'
@api_view(['GET','PUT','DELETE'])
def EventView(request, id):
    """
    API endpoint that allows events to be viewed, deleted or edited.
    """
    try:
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def UpdateEvent(request, id):
    try:
        event = Event.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
            serializer = EventSerializer(event, data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["sucess"] = "Updated Successfully!"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# To get an session by 'id'
@api_view(['GET','PUT','DELETE'])
def SessionView(request, id):
    """
    API endpoint that allows sessions to be viewed, deleted or edited.
    """
    try:
        event = Session.objects.get(id=id)
        serializer = SessionSerializer(event)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

# To list all events.
@api_view(['GET'])
def EventViewList(request):
    #try:
    queryset = Event.objects.all().order_by('start_date')
    serializer = EventSerializer(queryset, many=True)
    return Response(serializer.data)
    #except:
    #    return Response(status=status.HTTP_404_NOT_FOUND)

# To list all sessions.
@api_view(['GET'])
def SessionViewList(request):
    try:
        queryset = Session.objects.all().order_by('start_date')
        serializer = SessionSerializer(queryset, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)