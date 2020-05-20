from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post

# Create your views here.

#this view displays a list of posts
def post_list(request):
    object_list=Post.objects.all() #all objects

    paginator=Paginator(object_list,3) #3 posts per page



    page=request.GET.get('page')

    try:
        posts=paginator.page(page)

    except PageNotAnInteger:
        #if page is not an even integer, deliver first page
        posts=paginator.page(1)

    except EmptyPage:
        # if page is out of range, deliver the last page of results
        posts=paginator.page(paginator.num_pages)

    return render(request,'blog/post_list.html',{'page':page,'posts':posts})



#this view displays a detail of a single post
def post_detail(request,slug):
    post=Post.objects.get(slug=slug)

    return render(request,'blog/post_detail.html',{'post':post})
