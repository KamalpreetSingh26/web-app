from django.shortcuts import render,HttpResponse
from blog.models import Post
import math
# Create your views here.
def bloghome(request):
    no_of_posts=4
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page = int(page)
    allposts=Post.objects.all()
    length = len(allposts)
    allposts=Post.objects.all()[(page-1)*no_of_posts: page*no_of_posts]

    print(length)
    if page>1:
        prev=page-1
    else:
        prev = None

    if page<math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context={'allposts':allposts,'prev':prev,'nxt':nxt}
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request,'blog/blogpost.html',context)


