from django.shortcuts import render,HttpResponse

# Create your views here.
def post_index(request):
    return HttpResponse('burası anasayfa')

def post_detail(request):
    return HttpResponse('burası detay sayfası')

def post_create(request):
    return HttpResponse('burası oluşturma sayfası')

def post_update(request):
    return HttpResponse('burası güncelleme sayfası')

def post_delete(request):
    return HttpResponse('burası silme sayfası')




