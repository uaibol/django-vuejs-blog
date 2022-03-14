from django.shortcuts import render, redirect, Http404
from .forms import PostForm
from django.contrib import  messages
from .models import Post

def post_create(request):

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Post successfully created")
        return redirect('frontpage')
    context = {
        "form": form,
    }
    return render(request, 'post/form.html', context)

def post_detail(request, id):
    if request.method == 'GET':
        if Post.objects.filter(pk=id).exists():
            post = Post.objects.get(pk=id)
            post.increase_view_count()
            context = {
                "post":post,
            }
            return render(request, 'post/detail.html', context)
        return redirect('/')
    return redirect('/')

    
