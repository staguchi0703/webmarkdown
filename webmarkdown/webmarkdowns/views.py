from django.http import HttpResponse, HttpResponseRedirect
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Items, Logs
from blogs.models import Blog

from urllib.parse import urlencode

class IndexView(LoginRequiredMixin, ListView):
    template_name = 'items/index.html'
    model = Items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = set(Items.objects.values_list('category', flat=True))
        context["infos"] = Blog.objects.order_by('-update_datetime')[:3]
        return context

index = IndexView.as_view()

