from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request,'blog/index.html', context)

def archives(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request,'blog/archives.html', context)

def post(request, post_id):
    try:
        post = Post.objects.get(id=str(post_id))
    except Post.DoesNotExist:
        raise Http404
    context = {'post':post}
    return render(request, 'blog/post.html', context)

