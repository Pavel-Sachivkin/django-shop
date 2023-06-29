from django.views.generic import ListView, DetailView
from .models import Product, Category


class Catalog(ListView):
    model = Product
    template_name = 'catalog.jinja'
    context_object_name = 'categories'
    products = None

    def get_context_data(self, **kwargs):
        context = super(Catalog, self).get_context_data(**kwargs)
        context['title'] = 'Django-shop catalog'
        context['categories'] = Category.objects.all()
        context['products'] = self.products.order_by('?')
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(Catalog, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.products = Product.objects.filter(is_active=True)
        return self.products


class CategoryDetail(DetailView):
    model = Category
    template_name = 'catalog.jinja'
    context_object_name = 'category'
    category = None

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['title'] = 'Django-shop category ' + str(self.category.name)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(is_active=True, categories=self.category).order_by('?')
        context['random_products'] = Product.objects.filter(is_active=True).order_by('?')[:4]
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDetail, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk')
        self.category = Category.objects.get(id=pk)
        return self.category


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.jinja'
    context_object_name = 'product'
    product = None

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['title'] = 'Django-shop product ' + str(self.product.name)
        context['random_products'] = Product.objects.filter(is_active=True).exclude(id=self.product.id).order_by('?')[:4]
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(ProductDetail, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk')
        self.product = Product.objects.get(id=pk)
        return self.product