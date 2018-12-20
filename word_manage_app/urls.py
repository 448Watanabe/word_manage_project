from django.urls import path

from . import views

app_name = 'word_manage_app'
# このapp_nameは何の為？

urlpatterns = [
    path('index', views.index, name='index'),
    path('staticTest', views.staticTest, name = 'staticTest'),
    path('<int:word_id>/detail', views.detail, name = 'detail'),

]