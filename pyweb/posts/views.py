from django.shortcuts import render

# Create your views here.

def post_list_v(request):
    return render(request,'post_\post_list.html')
