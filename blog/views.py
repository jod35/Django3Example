from django.shortcuts import render

# Create your views here.

#this view displays a list of posts
def post_list(request):
    posts=Post.objects.all()
    return render('blog/post_list.html',{'posts':posts})


#this view displays a detail of a single post
def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,
    slug=post,
    status='published',
    publish_year=year,
    publish_month=month,
    publish_day=day
    )

    return render(request,'blog/post_detail.html',{'post':post})
