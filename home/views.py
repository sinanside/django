from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    data = {
    'isim': 'Umut'
    }
    return render(request,'home.html',data)
