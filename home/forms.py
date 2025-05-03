from django import forms
from authentication.models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_image',
            'batch_no',
            'blood_grp',
            'department',
            'semester',
            'section',
            'facebook_link',
            'linkedin_link',
            'instragram_link'
        ]
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'hidden'}),
            'full_name': forms.TextInput(attrs={
                'class': 'w-full bg-white/10 border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20',
                'required': True
            }),
            # Add similar widget definitions for other fields
        }