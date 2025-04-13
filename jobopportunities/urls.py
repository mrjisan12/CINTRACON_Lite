from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobopportunities, name="jobopportunities"),
]
