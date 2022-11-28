from django.urls import path
from .views import SignUpView, CustomerDetailView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
