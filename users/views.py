from django.shortcuts import render, redirect
from django.contrib import messages # this will allow us to send flash messages
from .forms import UserRegistrationForm # import the form we built in forms.py

def register(request):
    if request.method == 'POST': # If we are making a post request, then check if valid, if so, grab the username and store as a var
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save user to db and hash pw
            form.save()
            # Grab username from form so we can send flash message upon sign up
            username = form.cleaned_data.get('username')
            messages.success(request, f'New account created for {username}!')
            return redirect('renoreddit-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
