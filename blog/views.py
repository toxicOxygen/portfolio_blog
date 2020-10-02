from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import SharePostForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail


# Create your views here.
# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list,3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request,'blog/post/list.html',{'posts':posts,'page':page})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request,year,month,day,post):
    post_r = get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day,status='published')
    return render(request,'blog/post/detail.html',{'post':post_r})


def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status='published')
    sent = False

    if request.method == 'POST':
        #validate and clean form data
        form = SharePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_url(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['sender_email']}) recommends you read {post.title}"
            message = f'Read "{post.title}" at {post_url} '

            send_mail(subject,message,cd['sender_email'],[cd['receipient_email']])
            sent = True

    else:
        form = SharePostForm()
        return render(request,'',{'form':form,'post':post})