from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/react/<str:reaction_type>/', views.react_to_post, name='react_to_post'),
    
]
