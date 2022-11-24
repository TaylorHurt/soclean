from django.views.generic import ListView
from .models import Schedule


class HomePageView(ListView):
    model = Schedule
    template_name = "home.html"
