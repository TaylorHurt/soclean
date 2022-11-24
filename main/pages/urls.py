# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, SignUpView
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("", HomePageView.as_view(), name="home"),
]
