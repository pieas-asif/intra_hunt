from django.shortcuts import render

from .forms import NewsletterForm, HeroJobSearchForm


def home_page(request):
    newsletter_form = NewsletterForm()
    search_form = HeroJobSearchForm()
    context = {
        'newsletter_form': newsletter_form,
        'search_form': search_form,
    }
    return render(request, 'home/pages/home.html', context)


def landing_page(request):
    form = NewsletterForm()
    context = {
        'form': form
    }
    return render(request, 'home/pages/landing.html', context)
