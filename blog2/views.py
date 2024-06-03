from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, ResenPost, Tag, InstagramPost, Newsletter
from blog.form import ContactForm, Contact


def blog(request):
    posts = Blog.objects.all()
    categories = Category.objects.all()
    posts1 = ResenPost.objects.all()
    tags = Tag.objects.all()
    insta = InstagramPost.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'posts1': posts1,
        'tags': tags,
        'insta': insta
    }
    return render(request, 'blog.html', context)


def blog_detail(request, pk):
    post = get_object_or_404(Blog, id=pk)
    form = ContactForm()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    resenPost = ResenPost.objects.all()
    insta = InstagramPost.objects.all()
    newsletter = Newsletter.objects.all()
    comments = Contact.objects.filter(post__id=pk).order_by('-id')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f'/blog/{post.id}')
    contex = {
        'post': post,
        'form': form,
        'categories': categories,
        'tags': tags,
        'resenPost': resenPost,
        'insta': insta,
        'newsletter': newsletter,
        'comments': comments
    }
    return render(request, 'blog_details.html', contex)
