from django.urls import path
from .views import (
    
    EventView, 
    EventViewList, 
    SessionView, 
    SessionViewList, 
    UpdateEvent, 
    
    )

urlpatterns = [
    path('event/<id>/', EventView, name='detail'),
    path('event/<id>/update', UpdateEvent, name='detail'),
    path('event/', EventViewList),
    path('session/<id>/', SessionView),
    path('session/', SessionViewList),
]