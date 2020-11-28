from django.http import HttpResponse, HttpResponseRedirect
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Projects, Articles

from urllib.parse import urlencode

import markdown

def markd(txt):
    md = markdown.Markdown(extensions=['tables'])
    return md.convert(txt)



class IndexView(LoginRequiredMixin, ListView):
    template_name = 'webmarkdowns/index.html'
    model = Projects

index = IndexView.as_view()

def project(request, pjpk):
    project_name = get_object_or_404(Projects, pk=pjpk)
    article_list = Articles.objects.filter(project=project_name)
    html_article_list = []
    for article in article_list:
        html_article_list.append(markd(article.markdown_txt))
    return render(request, 'webmarkdowns/project.html', {'html_txt_list':html_article_list, 'articles':article_list, 'project_name':project_name})


def detail(request, pk):
    article_contents = Articles.objects.filter(pk=pk)
    return render(request, 'webmarkdowns/detail.html')


class NewsView(LoginRequiredMixin, ListView):
    template_name = 'webmarkdowns/news.html'
    model = Articles

news = NewsView.as_view()


class DeletesView(LoginRequiredMixin, ListView):
    template_name = 'webmarkdowns/delete.html'
    model = Articles

deletes = DeletesView.as_view()


class EditView(LoginRequiredMixin, ListView):
    template_name = 'webmarkdowns/edit.html'
    model = Articles

edit = EditView.as_view()

