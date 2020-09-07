from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()

        if len(cleaned_data['first_name']) == 0 and len(cleaned_data['last_name']) == 0:
            raise ValidationError("You need to fill at least one of the name fields")

        return cleaned_data
