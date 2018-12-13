from django.urls import path

from . import views

app_name = 'word_manage_app'
# このapp_nameは何の為？

urlpatterns = [
    path('index', views.index, name='index'),
    path('words', views.word, name='word'),
    path('<int:word_id>/detail', views.detail, name = 'detail'),
]