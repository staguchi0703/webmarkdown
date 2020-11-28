from django.urls import path
from . import views

app_name = 'webmarkdowns'

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pjpk>', views.project, name='project'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('news/<int:pk>', views.news, name='news'),
    path('deletes/<int:pk>', views.deletes, name='deletes'),
    path('edit/<int:pk>', views.edit, name='edit')

]

# pj-pk:プロジェクトのPK
# art-pk:記事のpk
# 新規はページにフォームを設けてprojectを指定させる
# プロジェクト内で新規作成するときは別のプロジェクトに飛ばない様に固定値で処理する
