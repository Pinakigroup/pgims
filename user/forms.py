from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class ProfileForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    designation = forms.CharField(max_length=64, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'designation', 'password1', 'password2']  
        
    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.designation = self.cleaned_data["designation"]
        if commit:
            user.save()
        return user  