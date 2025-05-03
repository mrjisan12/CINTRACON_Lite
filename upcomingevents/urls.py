from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcomingevents, name="upcomingevents"),
    path('create/upcoming-event/', views.create_upcoming_event, name="create_upcoming_event")
]
