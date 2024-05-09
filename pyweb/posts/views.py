from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list_v(request):
    post_ob= Post.objects.all()
    return render(request,'post_\post_list.html',{'post':post_ob})
