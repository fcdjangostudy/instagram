from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from member.models import User
from .forms import PostCreate, PostModify
from .models import Post


def post_list(request):
    # 모든 Post목록을 'posts'라는 key로 context에 담아 return render처리
    # css/post_list.html을 template으로 사용하도록 한다

    # 각 포스트에 대해 최대 4개까지의 댓글을 보여주도록 템플릿에 설정
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'css/post_list.html', context)


def post_detail(request, post_pk):
    # post_pk에 해당하는 Post객체를 리턴, 보여줌
    post = get_object_or_404(Post, pk=post_pk)
    # 구식 방식
    # template = loader.get_template('css/post_detail.html')
    # context = {
    #     'css': css,
    # }
    # rendering_string = template.render(context=context, request=request)
    # return HttpResponse(rendering_string)
    context = {
        'css': post
    }
    return render(request, 'css/post_detail.html', context)


def post_create(request):
    # POST요청을 받아 Post객체를 생성 후 post_list페이지로 redirect
    if request.method == 'GET':
        form = PostCreate()
        context = {
            'form': form,
        }
        return render(request, 'css/post_create.html', context)
    elif request.method == 'POST':
        form = PostCreate(request.POST, request.FILES)
        if form.is_valid():
            author = User.objects.first()
            photo = request.FILES['photo']
            Post.objects.create(
                author=author,
                photo=photo,
            )
            return redirect('css:post_list')

    else:
        form = PostCreate()
        context = {
            'form': form,
        }
        return render(request, 'css/post_create.html', context)


def post_modify(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'GET':
        form = PostModify()
        context = {
            'css': post,
            'forms': form,
        }
        return render(request, 'css/post_modify.html', context)
    elif request.method == 'POST':
        form = PostModify(request.POST, request.FILES)
        if form.is_valid():
            photo = request.FILES["photo"]
            post.photo = photo
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_delete(request, post_pk):
    # post_pk에 해당하는 Post에 대한 delete요청만을 받음
    # 처리완료후에는 post_list페이지로 redirect
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('css:post_list')

    elif request.method == 'GET':
        return redirect('css:post_detail', post_pk=post.pk)


def comment_create(request, post_pk):
    # POST요청을 받아 Comment객체를 생성 후 post_detail페이지로 redirect
    pass


def comment_modify(request, post_pk):
    # 수정
    pass


def comment_delete(request, post_pk, comment_pk):
    # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    pass
