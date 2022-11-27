from django.urls import path
from .views import SignUpView, CustomerDetailView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("customer_detail/", CustomerDetailView.as_view(), name="customer_detail"),
]
