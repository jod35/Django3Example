from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

#this view displays a list of posts
def post_list(request):
    posts=Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})


#this view displays a detail of a single post
def post_detail(request,id):
    post=Post.objects.get(id=id)

    return render(request,'blog/post_detail.html',{'post':post})
