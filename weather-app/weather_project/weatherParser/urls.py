from django.views.generic import RedirectView
from django.urls import path
# Импортируем views из папки приложения weatherParser
from django.conf.urls.static import static
from .import views
#
urlpatterns = [
    path('', views.index),# метод index в файле weatherParser/views
    path('add/', views.addData),# метод addDate в файле weatherParser/views
    path('del/', views.delTable),# метод delTable в файле weatherParser/views
]