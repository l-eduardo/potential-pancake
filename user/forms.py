from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms

        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']
        
class EmailOnlyPasswordResetForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email']
        
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UpdateUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class UpdateEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class UpdatePasswordForm(UserChangeForm):
    class Meta:
        model = User
        fields = ()

    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)
        del self.fields['username']
        del self.fields['first_name']
        del self.fields['last_name']
        del self.fields['email']
        del self.fields['is_active']
        del self.fields['is_staff']
        del self.fields['is_superuser']
