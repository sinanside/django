# from django.contrib import admin
from baton.autodiscover import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publiishing_date']
    list_display_links = ['publiishing_date']
    list_filter = ['publiishing_date']
    search_fields = ['title', 'content']
    list_editable = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)

