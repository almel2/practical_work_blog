from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel
from django import forms


class CastomUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = UserCreationForm.Meta.fields + ('email',)
