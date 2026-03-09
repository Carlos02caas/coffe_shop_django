from django.views import generic
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list_products.html"
    context_object_name = "products"

class homeView(generic.TemplateView):
    template_name = "products/home.html"