from django.urls import path
from blog import views


urlpatterns = [
    path('', views.index, name='home'),
    path('post-list/', views.PostList.as_view(), name='post_list'),
    path('user-posts/', views.UserPostList.as_view(), name='user_posts'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
