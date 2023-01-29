from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    designation = forms.CharField(max_length=64, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'designation', 'password1', 'password2']  
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.designation = self.cleaned_data["designation"]
        if commit:
            user.save()
        return user      

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user  
 
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']    
 
 
 
# class UserProfileForm(forms):
#     class Meta:
#         model = User 
#         fi