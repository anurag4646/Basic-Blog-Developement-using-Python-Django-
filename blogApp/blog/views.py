from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# from .models import Post
# from .forms import CommentForm
# from django.shortcuts import render, get_object_or_404


# Create your views here. 

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html' , context)

def blogPost(request , slug):
    post = Post.objects.filter(slug = slug ).first()
    context = {'post':post}
    return render(request, 'blog/blogPost.html', context)


