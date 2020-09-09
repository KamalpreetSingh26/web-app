from django.contrib import admin
from django.urls import path,include
from blog import views
urlpatterns = [
    
    path('',views.bloghome,name="bloghome"),
    path('blogpost',views.blogpost,name="blogpost"),
    path('<str:slug>',views.blogpost,name="blogpost"),
    
]