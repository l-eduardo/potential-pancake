from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User

        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class EditPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['current_password', 'new_password1', 'new_password2']


class EmailOnlyPasswordResetForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email']
        
    