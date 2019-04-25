from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    data = {
    'isim': 'Umut'
    }
    return render(request,'home.html',data)


def about_view(request):
    data = {
        'isim': 'Umut'
    }
    return render(request, 'home.html', data)


def contact_view(request):
    data = {
        'isim': 'Umut'
    }
    return render(request, 'home.html', data)
