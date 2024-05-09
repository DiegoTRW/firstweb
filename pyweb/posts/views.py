
from django.shortcuts import render
from .models import Post

def post_list_v(request):
    posts = Post.objects.all()
    return render(request, 'post_/post_list.html', {'posts': posts})
