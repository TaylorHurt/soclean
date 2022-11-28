# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # new
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Review


class ReviewListView(ListView):
    model = Review
    template_name = "review_list.html"


class ReviewDetailView(DetailView):  # new
    model = Review
    template_name = "review_detail.html"


class ReviewUpdateView(UpdateView):  # new
    model = Review
    fields = (
        "title",
        "body",
    )
    template_name = "review_edit.html"

    def test_func(self):  # new
        obj = self.get_object()
        # Allow superuser to update article.
        return obj.author == self.request.user or self.request.user.is_superuser


class ReviewDeleteView(DeleteView):  # new
    model = Review
    template_name = "review_delete.html"
    success_url = reverse_lazy("review_list")

    def test_func(self):  # new
        obj = self.get_object()
        # Allow superuser to delete article.
        return obj.author == self.request.user or self.request.user.is_superuser


class ReviewCreateView(CreateView):  # new
    model = Review
    template_name = "review_new.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):  # new
        form.instance.author = self.request.user
        return super().form_valid(form)
