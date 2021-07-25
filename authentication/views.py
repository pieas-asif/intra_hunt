from django.shortcuts import render, redirect
from django.contrib import messages

from authentication.forms import UserRegistrationForm
from home.forms import NewsletterForm


def auth_home_view(request):
    return render(request, 'authentication/home.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        newsletter_form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
        newsletter_form = NewsletterForm()
    context = {
        'form': form,
        'newsletter_form': newsletter_form
    }
    return render(request, 'authentication/register.html', context)