from django.urls import path
from .import views # Импортируем views из папки приложения weatherParser
#
urlpatterns = [
    path('', views.weatherParser),# метод index в файле weatherParser/views
]