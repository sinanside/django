from django.shortcuts import render
from forms import ContactForm
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
    contact_form = ContactForm()
    data = {
        'title': 'İletişim sayfası',
        'content': 'İletişim formumuzu doldurunuz.',
        'form': contact_form
    }
    return render(request, 'contact.html', data)
