from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_sharing, name="notes_sharing"),
    path('notes/<int:semester_id>/', views.semester_notes, name='semester_notes'),
]