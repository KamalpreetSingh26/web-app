from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.models import Contact
from datetime import datetime
from blog.models import Post
from home.models import Author
import math

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        if len(name)<4 or len(email)<10 or len(phone)<10 or len(phone)>10:
            messages.error(request,"Please fill the Contact form correctly!!")
        else:
            contact=Contact(name=name,email=email,phone=phone,message=message)
            contact.save()
            messages.success(request,"Your message has been successfully submitted :)")

    return render(request,'home/contact.html')

def about(request):
    
    return render(request,'home/about.html')



def search(request):
    query = request.GET['query']
    allposts = Post.objects.filter(title__icontains=query)
    if len(query)>25 or len(query)<=3:
        messages.warning(request,"Your search is too long or too short.Please use other keywords")
        return render(request,'home/search.html')
    else:
      params = {"allposts":allposts,'query':query}
      return render(request,'home/search.html',params)






        
        
    






def author(request):
    no_of_posts=2
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page = int(page)
    authors=Author.objects.all()
    length = len(authors)
    authors=Author.objects.all()[(page-1)*no_of_posts: page*no_of_posts]

    print(length)
    if page>1:
        prev=page-1
    else:
        prev = None

    if page<math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context={'authors':authors,'prev':prev,'nxt':nxt}
    return render(request,'blog/authors.html',context)