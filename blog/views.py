from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm

# Create your views here.
class PostListView(ListView):
    queryset=Post.objects.all()
    context_object_name='posts'
    paginate_by=3
    template_name='blog/post_list.html'

#this view displays a list of posts
'''def post_list(request):
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

    return render(request,'blog/post_list.html',{'page':page,'posts':posts})'''



#this view displays a detail of a single post
def post_detail(request,post_id):
    post=Post.objects.get(id=post_id)

    return render(request,'blog/post_detail.html',{'post':post})


def post_share(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    sent=False

    if request.method == "POST":
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_url(post.get_absolute_url())
            subjects=f"{cd['name']} recommends you read {cd['title']}"
            message=f"Read {post.title} at {post_url} \n"
            send_mail(subject,message,'jodestrevin@gmail.com',[cd['to']])

            sent=True

    else:
        form=EmailPostForm()

    context={
        'post':post,
        'form':form,
         'sent':sent
    }

    return render(request,'blog/post_share.html',context)
