from django.contrib import admin
from django.conf.urls import url, include
from home.views import home_view, about_view, contact_view, login_page, register_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view),
    url(r'^home/', include('home.urls')),
    url(r'^about/$', about_view),
    url(r'^login/$', login_page),
    url(r'^register/$', register_page),
    url(r'^contact/$', contact_view),
    url(r'^products/', include("products.urls")),

    url(r'^post/', include('post.urls')),
    ]
