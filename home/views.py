from django.shortcuts import render
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
    return render(request, 'about.html', data)


def contact_view(request):
    data = {
        'title': 'İletişim sayfası',
        'content': 'İletişim formumuzu doldurunuz.'
    }
    return render(request, 'contact.html', data)
