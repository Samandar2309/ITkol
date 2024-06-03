from django.shortcuts import render

from .form import ContactForm
from .models import Post, Single_offers, Category_name, Category, Information, Numbers, Case, Blog, Video


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')[:3]
    single_offers = Single_offers.objects.all().order_by('-id')[:3]
    categories = Category.objects.all().order_by('id')[:4]
    category_names = Category_name.objects.all()
    information = Information.objects.all().order_by('-id')[:1]
    numbers = Numbers.objects.all()
    cases = Case.objects.all().order_by('id')[:3]
    videos = Video.objects.all().order_by('id')[:1]
    context = {
        'posts': posts,
        'single_offers': single_offers,
        'categories': categories,
        'category_names': category_names,
        'information': information,
        'numbers': numbers,
        'cases': cases,
        'videos': videos

    }
    return render(request, 'index.html', context)


def services(request):
    posts = Post.objects.all()
    categories = Category.objects.all().order_by('id')[:4]
    category_names = Category_name.objects.all()
    videos = Video.objects.all().order_by('id')[:1]
    contex = {
        'posts': posts,
        'categories': categories,
        'category_names': category_names,
        'videos': videos
    }
    return render(request, 'services.html', contex)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = ContactForm()
    contex = {
        'form': form,

    }
    return render(request, 'contact.html', contex)


def about(request):
    about1 = Blog.objects.all()
    numbers = Numbers.objects.all()
    information = Information.objects.all().order_by('id')[:1]
    videos = Video.objects.all().order_by('id')[:1]
    single_offers = Single_offers.objects.all().order_by('-id')[:3]
    contex = {
        'about': about1,
        'numbers': numbers,
        'information': information,
        'videos': videos,
        'single_offers': single_offers
    }
    return render(request, 'about.html', contex)


def cases(request):
    cases1 = Case.objects.all().order_by('id')[:3]
    videos = Video.objects.all().order_by('id')[:1]
    contex = {
        'cases': cases1,
        'videos': videos
    }
    return render(request, 'case_study.html', contex)
