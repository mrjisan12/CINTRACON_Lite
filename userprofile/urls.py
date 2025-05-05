from django.urls import path 
from . import views

urlpatterns = [
    path('profile/<int:id>',views.user_profile, name="profile"),
    path('profile/<int:id>/edit/', views.edit_profile, name='edit_profile'),
]
