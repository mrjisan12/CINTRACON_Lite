from django.shortcuts import render

def landingPage(request):
    return render(request, 'landingPage.html')

def loginPage(request):
    return render(request, 'LoginPage/loginPage.html')


def signupPage(request):
    return render(request, 'SignupPage/signupPage.html')