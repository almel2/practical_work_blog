from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    STATUS = [
        ('DRA', 'Draft'),
        ('PUB', 'Published'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS, default='Draft')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
