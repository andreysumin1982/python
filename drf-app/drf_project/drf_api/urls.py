from django.views.generic import RedirectView # Нужно для иконки во вкладке
from django.urls import path # include уже не нужно использ.
from . import views # обязательно импортируем файл views
urlpatterns = [
    path('', views.index, name='index'), # здесь уже использ. файл views и метод index в этом файле
    path('api/v1/test/', views.testApi, name='testApi'),
    path('api/v2/test2/', views.testApi2, name='testApi2'),

    #-Иконка-#
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)) # Нужно для иконки во вкладке
]