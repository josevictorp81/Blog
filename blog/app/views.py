from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post, Contact
from .forms import ContactModelForm

# Create your views here.
def index(request):
    post = Post.objects.filter(deleted=False)

    data = {
        'post':post,
    }
    return render(request, 'index.html', data)

def postDetail(request, id):
    post = Post.objects.get(id=id)
    
    data = {
        'post': post
    }
    return render(request, 'postDetail.html', data)

def form(request):
    if str(request.method) == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')
    '''name = request.POST['name']
    Contact.objects.create(
        name = name,
        email = request.POST['email'],
        message = request.POST['message']
    )
    data = {
        'name': name
    }'''
    return render(request, 'contato.html')