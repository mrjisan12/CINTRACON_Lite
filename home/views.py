from django.shortcuts import render

# Create your views here.
def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Pass the user's full name to the template
        context = {'full_name': request.user.full_name}
    else:
        context = {}
    return render(request,'HomePage/homePage.html', context)