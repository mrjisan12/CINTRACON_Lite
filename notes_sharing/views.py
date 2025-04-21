from django.shortcuts import render

# Create your views here.
def notes_sharing(request):
    return render(request,'NotesSharing/notes_sharing.html')