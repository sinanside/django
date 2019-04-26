from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, **kwargs):
        data = super(ProductListView, self).get_context_data(**kwargs)
        return data


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, "products/list.html", context)
