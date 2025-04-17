from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.

# def loginPage(request):
#     return render(request, 'LoginPage/loginPage.html')


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Get the username (email)
            password = form.cleaned_data.get('password')  # Get the password
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to the home page or dashboard after successful login
            else:
                # If authentication fails, show error
                form.add_error(None, "Invalid username or password.")
        else:
            # If the form is invalid
            form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'LoginPage/loginPage.html', {'form': form})


def signupPage(request):
    return render(request, 'SignupPage/signupPage.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the user and profile to the database
            return redirect('home')  # Redirect to the homepage or login page after successful registration
        else:
            # If the form is not valid, you can add error handling
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'SignupPage/signupPage.html', {'form': form})


