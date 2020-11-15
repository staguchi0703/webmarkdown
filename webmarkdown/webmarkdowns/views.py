from django.http import HttpResponse, HttpResponseRedirect
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Projects, Articles

from urllib.parse import urlencode

class IndexView(LoginRequiredMixin, ListView):
    template_name = 'webmarkdowns/index.html'
    model = Articles

index = IndexView.as_view()

