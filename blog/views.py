from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

User = get_user_model()


def index(request):
    return render(request, 'blog/index.html', context={})


class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()


class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.all()
    pk_url_kwarg = 'pk'
    template_name = 'blog/post_detaile.html'


class UserPostList(ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'blog/user_posts_list.html'
    context_object_name = 'users'


class ProfilePublic(DetailView):
    model = User
    queryset = User.objects.all()
    context_object_name = 'users'
    pk_url_kwarg = 'pk'
    template_name = 'blog/profile_public.html'
