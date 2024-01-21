from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # This creates a form we can pass to the front end
from django.contrib import messages # this will allow us to send flash messages

def register(request):
    if request.method == 'POST': # If we are making a post request, then check if valid, if so, grab the username and store as a var
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'New account created for {username}!')
            return redirect('renoreddit-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
