from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import NewsletterForm, HeroJobSearchForm
from .models import Post


def home_page(request):
    newsletter_form = NewsletterForm()
    search_form = HeroJobSearchForm()
    context = {
        'newsletter_form': newsletter_form,
        'search_form': search_form,
    }
    return render(request, 'home/pages/home.html', context)


@login_required
def landing_page(request):
    form = NewsletterForm()
    context = {
        'newsletter_form': form
    }
    return render(request, 'home/pages/landing.html', context)


def post_page(request):
    form = NewsletterForm()
    context = {
        'newsletter_form': form,
        'post': Post.objects.first()
    }
    return render(request, 'home/pages/post.html', context)


def find_work_view(request):
    form = NewsletterForm()
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    context = {
        'newsletter_form': form,
        'posts': paginator.get_page(page_number)
    }
    return render(request, 'home/pages/find_work.html', context)
