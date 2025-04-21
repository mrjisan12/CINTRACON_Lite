from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_sharing, name="notes_sharing"),
]