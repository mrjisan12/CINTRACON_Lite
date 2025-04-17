from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    department = forms.ChoiceField(choices=UserProfile.DEPARTMENTS)
    semester = forms.ChoiceField(choices=UserProfile.SEMESTERS)
    section = forms.ChoiceField(choices=UserProfile.SECTIONS)
    batch_no = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password1', 'password2', 'department', 'semester', 'section', 'batch_no']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        if commit:
            user.save()

            # Create the user profile after the user is created
            UserProfile.objects.create(
                user=user,
                department=self.cleaned_data.get('department', 'CSE'),
                semester=self.cleaned_data.get('semester', '1.1'),
                section=self.cleaned_data.get('section', 'A'),
                batch_no=self.cleaned_data.get('batch_no', '1'),
                
            )
        return user
