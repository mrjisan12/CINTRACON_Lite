"""
URL configuration for cintracon_lite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static
from authentication import views as auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landingPage, name="landingPage"),
    path('login/', auth.loginPage, name="loginPage"),
    path('signup/', auth.signupPage, name="signupPage"),
    path('register/', auth.register, name='register'),
    path('logout/', auth.logout_view, name='logout'),
    path('home/', include('home.urls')),
    path('allstudents/', include('allstudents.urls')),
    path('job-opportunities/', include('jobopportunities.urls')),
    path('notes_sharing/',include('notes_sharing.urls')),
    path('upcoming-events/',include('upcomingevents.urls')),
    path('Announcement/',include('Announcement.urls')),
    path('user/', include('userprofile.urls')),
    
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
