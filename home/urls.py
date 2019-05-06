from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$', home_view),
    url(r'^arduino_led_yak_sondur/$', ledyaksondur_view),
    url(r'^hakkımızda/$', hakkımızda_view),

]
