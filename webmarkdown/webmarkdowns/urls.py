from django.urls import path
from . import views

app_name = 'webmarkdowns'

urlpatterns = [
    path('', views.index, name='index'),

]

