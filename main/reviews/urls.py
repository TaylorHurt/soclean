from django.urls import path

from .views import (
    ReviewListView,
    ReviewDetailView,
    ReviewUpdateView,
    ReviewDeleteView,
    ReviewCreateView,  # new
)

urlpatterns = [
    path("<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("<int:pk>/edit/", ReviewUpdateView.as_view(), name="review_edit"),
    path("<int:pk>/delete/", ReviewDeleteView.as_view(), name="review_delete"),
    path("new/", ReviewCreateView.as_view(), name="review_new"),  # new
    path("", ReviewListView.as_view(), name="review_list"),
]
