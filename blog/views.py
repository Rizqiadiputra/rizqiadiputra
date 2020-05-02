from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def daftar_post(request):
    posts_diobjectview = Post.objects.filter(tgl_terbit__lte=timezone.now()).order_by('tgl_buat')
    # print(posts_diobjectview)
    #{} = tempat dimana kita dapat menambahkan sesuatu untuk digunakan di template
    return render(request, 'blog/daftar_post.html', {'posts_ditemplate':posts_diobjectview})