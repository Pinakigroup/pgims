from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    birthdate = forms.DateField()
    discord_id = forms.CharField(max_length=100, help_text='Discord ID')
    zoom_id = forms.CharField(max_length=100, help_text='Zoom ID')
    
    designation = forms.CharField(max_length=64, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'designation', 'birthdate', 'discord_id', 'zoom_id', 'password1', 'password2'] 
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.designation = self.cleaned_data["designation"]
        user.birthdate = self.cleaned_data["birthdate"]
        user.discord_id = self.cleaned_data["discord_id"]
        user.zoom_id = self.cleaned_data["zoom_id"]
        if commit:
            user.save()
        return user   