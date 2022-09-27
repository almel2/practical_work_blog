from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

User = get_user_model()


def index(request):
    return render(request, 'blog/index.html', context={})


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        comment = form.cleaned_data['comment']
        post = Post.objects.get(pk=int(self.kwargs['pk']))
        form.instance.post = post
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        send_mail('Blog info', f'Check a new comment {comment}',
                  'blog@gmail.com',
                  ['admin@gmail.com'])
        return super(CommentCreate, self).form_valid(form)


class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.select_related('author').prefetch_related('comment_set__author').filter(status='PUB')
    paginate_by = 2


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'

    def get_success_url(self):
        return reverse_lazy('profile_public', kwargs={'pk': self.request.user.id})

    def form_valid(self, form):
        # self.object = form.save(commit=False)
        form.instance.author = self.request.user
        send_mail('Blog info', 'Check a new comment post', 'blog@gmail.com', ['admin@gmail.com'])
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'

    def get_success_url(self):
        return reverse_lazy('profile_public', kwargs={'pk': self.request.user.id})


class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.all()
    pk_url_kwarg = 'pk'
    template_name = 'blog/post_detaile.html'


class UserPostList(ListView):
    model = User
    queryset = User.objects.prefetch_related('post_set')
    template_name = 'blog/user_posts_list.html'
    context_object_name = 'users'


class ProfilePublic(DetailView):
    model = User
    context_object_name = 'user'
    pk_url_kwarg = 'pk'
    template_name = 'blog/profile_public.html'
