from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("list_products")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # login automático
        return response
