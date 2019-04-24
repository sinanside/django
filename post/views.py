from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.
def post_index(request):
    posts = Post.objects.all()
    return render(request,'post/index.html',{'posts': posts })

def post_detail(request):
    return HttpResponse('burası detay sayfası')

def post_create(request):
    return HttpResponse('burası oluşturma sayfası')

def post_update(request):
    return HttpResponse('burası güncelleme sayfası')

def post_delete(request):
    return HttpResponse('burası silme sayfası')




