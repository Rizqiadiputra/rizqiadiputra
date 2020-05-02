from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import FormPost


# Create your views here.
def daftar_post(request):
    posts_diobjectview = Post.objects.filter(tgl_terbit__lte=timezone.now()).order_by('tgl_buat')
    # print(posts_diobjectview)
    #{} = tempat dimana kita dapat menambahkan sesuatu untuk digunakan di template
    return render(request, 'blog/daftar_post.html', {'posts_ditemplate':posts_diobjectview})

#pk = primary key = unique identifier for each record in a database
#django secara default membuat id per data sebagai pk
def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail_post.html', {'post':post})

def baru_post(request):
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.penulis = request.user
            post.tgl_terbit = timezone.now()
            post.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = FormPost()
    return render(request, 'blog/edit_post.html', {'form':form})

def edit_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = FormPost(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.penulis = request.user
            post.tgl_terbit = timezone.now()
            post.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = FormPost(instance=post)
    return render(request, 'blog/edit_post.html', {'form':form})