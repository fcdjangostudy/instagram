"""
member application생성
    User모델 구현
        username, nickname
이후 해당 User모델을 Post나 Comment에서 author나 user항목으로 참조
"""
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    photo = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        User,
        related_name='like_users'
    )
    tag = models.ManyToManyField('Tag')


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)


# class PostLike(models.Model):
#     pass


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag ({})'.format(self.name)
