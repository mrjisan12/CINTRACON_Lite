from django.urls import path
from . import views

urlpatterns = [
    path('', views.allStudents, name="allStudents"),
    path('search-students/', views.allStudents, name='search_students'),
]
