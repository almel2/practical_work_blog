from django.contrib import admin
from django.core.mail import send_mail

from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'content', 'status', 'create_date', 'update_date')
    readonly_fields = ('author', 'create_date', 'update_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'comment', 'post', 'is_published', 'create_date', 'update_date')
    readonly_fields = ('author', 'post', 'create_date', 'update_date')
    empty_value_display = 'Anonymous'
    list_filter = ('is_published',)
    ordering = ('create_date',)

    def save_model(self, request, obj, form, change):  # send email for public comment
        if obj.is_published and obj.author is not None:
            send_mail('Blog info',
                      f'''{obj.author} you have a new comment in post {obj.post.title},
                        link http://127.0.0.1:8000/post/{obj.post.id}/''',
                      'blog@gmail.com',
                      [obj.author.email, ]
                      )
        super().save_model(request, obj, form, change)
