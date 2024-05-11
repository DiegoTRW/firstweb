# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list_v,name="post"),
    path('<slug:slug>',views.post_page,name="page")
]
