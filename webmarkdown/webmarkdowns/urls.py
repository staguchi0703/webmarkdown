from django.urls import path
from . import views

app_name = 'webmarkdowns'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
    path('<int:pk>/news', views.news, name='news'),
    path('<int:pk>/deletes', views.deletes, name='deletes'),
    path('<int:pk>/edit', views.edit, name='edit')

]

# pj-pk:プロジェクトのPK
# art-pk:記事のpk
# 新規はページにフォームを設けてprojectを指定させる
# プロジェクト内で新規作成するときは別のプロジェクトに飛ばない様に固定値で処理する
