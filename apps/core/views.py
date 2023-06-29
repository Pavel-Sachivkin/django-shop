from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from shop.models import Product


class Home(TemplateView):
    template_name = 'index.jinja'
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Django-shop'
        context['random_products'] = Product.objects.filter(is_active=True).order_by('?')[:4]
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(Home, self).dispatch(request, *args, **kwargs)


def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "500.html", {})