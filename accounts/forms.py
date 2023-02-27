from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomCreateForms(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'age',)


class CustomChangeForms(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields