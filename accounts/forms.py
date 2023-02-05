from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Profile
from django import forms



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'img_profile', 'phone', 'designation', 'dob']
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']   

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['id', 'user', 'full_name', 'img_profile', 'email', 'phone', 'designation', 'dob']
#         widgets = {
#             'user': forms.Select(attrs={'class':'form-control'}),
#             'full_name': forms.TextInput(attrs={'class':'form-control'}),          
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'designation': forms.TextInput(attrs={'class': 'form-control'}),
#             'dob': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
#         }
#         labels = {
#             'img_profile': 'Photo',
#         } 

# def save(self, commit=True):
#     Profile = super(ProfileForm, self).save(commit=False)
#     Profile.Company_name(self.cleaned_data["Company_name"])

#     if commit:
#             Profile.save()
#     return Profile