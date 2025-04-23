from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcomingevents, name="upcomingevents"),
]
