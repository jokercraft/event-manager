from django.urls import path, include
from rest_framework import routers
from .views import (
    
    EventView, 
    SessionView, 
    
    )

router = routers.DefaultRouter()
router.register("events", EventView)
router.register("sessions", SessionView)

urlpatterns = [
    path('', include(router.urls)),
    ]