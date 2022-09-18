from django.contrib import admin
from django.core.mail import send_mail

from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):  # send email for public comment
        if obj.is_published and obj.user_id is not None:
            send_mail('Blog info',
                      f'''{obj.user_id} you have a new comment in post {obj.post.title},
                        link http://127.0.0.1:8000/post/{obj.post.id}/''',
                      'blog@gmail.com',
                      [obj.user_id.email, ]
                      )
        super().save_model(request, obj, form, change)
