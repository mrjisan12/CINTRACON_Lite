from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def notes_sharing(request):
    semesters = Semester.objects.all()
    return render(request,'NotesSharing/notes_sharing.html', {'semesters': semesters})

def semester_notes(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    notes = Note.objects.filter(semester=semester)
    return render(request, 'NotesSharing/semester_notes.html', {'semester': semester, 'notes': notes})
