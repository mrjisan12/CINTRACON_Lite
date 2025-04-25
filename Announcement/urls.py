from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcement_view, name="Announcement"),  
]
