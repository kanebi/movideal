from django.shortcuts import render

# Create your views here.

# example below
# def index(request):
#     context = {}
#     return render(request, 'index.html', context)

def blog_posts(request):
    context = {}
    return render(request, 'blog/blog_posts.html', context)
