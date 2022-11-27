from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser

from django.views.generic import (
    DetailView,
    CreateView,
)
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomerDetailView(DetailView):
    model = CustomUser
    template_name = "customer_detail.html"
