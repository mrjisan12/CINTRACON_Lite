from django.shortcuts import render

# Create your views here.
def allStudents(request):
    return render(request,'AllStudents/allStudentsPage.html')