from django.shortcuts import render, redirect
from django.contrib import messages

from authentication.forms import UserRegistrationForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,

    }
    return render(request, 'authentication/register.html', context)