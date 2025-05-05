from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def notes_sharing(request):
    semesters = Semester.objects.all()
    return render(request,'NotesSharing/notes_sharing.html', {'semesters': semesters})

def semester_notes(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    notes = Note.objects.filter(semester=semester).order_by('-uploaded_at')
    return render(request, 'NotesSharing/semester_notes.html', {'semester': semester, 'notes': notes})


@login_required
def add_note(request):
    if request.method == 'POST':
        semester_name = request.POST.get('semester')
        semester = get_object_or_404(Semester, name=semester_name)

        name = request.POST.get('name')
        description = request.POST.get('description')
        page_no = request.POST.get('page_no')
        file = request.FILES.get('file')

        if name and description and page_no and file:
            Note.objects.create(
                semester=semester,
                user=request.user,
                name=name,
                description=description,
                page_no=page_no,
                file=file
            )
            messages.success(request, "Note uploaded successfully!")
        else:
            messages.error(request, "All fields are required.")

        return redirect('semester_notes', semester_id=semester.id)
    else:
        messages.error(request, "Invalid request.")
        return redirect('notes_sharing')