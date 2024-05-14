
from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

def post_list_v(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'post_/post_list.html', {'posts': posts})


def post_page(request,slug):
    # return HttpResponse(slug)
    posts = Post.objects.get(slug=slug)
    return render(request, 'post_/post_page.html', {'posts': posts})