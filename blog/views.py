from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

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