"""
member application생성
    User모델 구현
        username, nickname
이후 해당 User모델을 Post나 Comment에서 author나 user항목으로 참조
"""
from django.db import models

# from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='css', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_posts',
        through='PostLike',
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True
    )

    def add_comment(self, user, content):
        return self.comment_set.create(
            author=user,
            content=content,
        )

    def add_tag(self, tag_name):
        tag, tag_created = Tag.objects.get_or_create(name=tag_name)
        if not self.tags.filter(name=tag_name).exists():
            self.tags.add(tag)
        return

    @property
    def like_count(self):
        return self.like_users.count()

    def __str__(self):
        return '{} / {}'.format(self.author, self.created_date)


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'post_post_like_users'


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='CommentLike',
        related_name='like_comments'
    )

    def __str__(self):
        return '{}/{}'.format(self.post, self.author)


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


# class PostLike(models.Model):
#     pass


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag ({})'.format(self.name)
