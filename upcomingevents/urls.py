from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcomingevents, name="upcomingevents"),
    path('create/upcoming-event/', views.create_upcoming_event, name="create_upcoming_event"),
    path('update_upcoming_event/<int:event_id>/', views.update_upcoming_event, name="update_upcoming_event"),
    path('delete_upcoming_event/<int:event_id>/', views.delete_upcoming_event, name="delete_upcoming_event"),

]
