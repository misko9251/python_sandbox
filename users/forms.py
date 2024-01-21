# This file exists so we can add an email field to our form - it inherits from the user creation form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # This creates a form we can pass to the front end

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField() # this defaults to required=True

    # Below we are specifying the model that we want this form to interact with
    class Meta:
        model = User
        # the fields we want to show in the form and the appropriate order
        fields = ['username', 'email', 'password1', 'password2']