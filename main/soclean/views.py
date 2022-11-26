from django.views.generic import ListView
from .models import Schedule
from django.views.generic import CreateView


class HomePageView(ListView):
    model = Schedule
    template_name = "home.html"
