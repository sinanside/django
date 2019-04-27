from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView

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
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = get_object_or_404(Product, slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Ürün bulunamadı")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("bilinmeyen bir hata oluştu")
        return instance

        data['test'] = 555
        return data


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        data = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        data['test'] = 555
        return data


def product_detail_view(request, pk=None):
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
