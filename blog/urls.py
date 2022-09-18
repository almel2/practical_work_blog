from django.urls import path
from blog import views


urlpatterns = [
    path('', views.index, name='home'),
    path('post-list/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post-create/', views.PostCreate.as_view(), name='post_create'),
    path('post-update/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),

    path('comment/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),

    path('user-posts/', views.UserPostList.as_view(), name='user_posts'),
    path('profile/<int:pk>/', views.ProfilePublic.as_view(), name='profile_public'),
]
