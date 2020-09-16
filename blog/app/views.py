from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):
    lista = [
        'django', 'python', 'git',
        'html'
    ]

    post = Post.objects.filter(deleted=False)

    data = {
        'name': 'curso django 3',
        'lista': lista,
        'post':post,
    }
    return render(request, 'index.html', data)

def postDetail(request, id):
    post = Post.objects.get(id=id)
    data = {
        'post': post
    }
    return render(request, 'postDetail.html', data)