from django.views.generic import RedirectView
from django.urls import path
#from django.conf.urls import url
# Импортируем views из папки приложения syslogParser
from django.conf.urls.static import static
from .import views

urlpatterns =[
    path('', views.index, name='index'),  # метод index в файле weatherParser/views
    #path('add/', views.addData, name='add'),  # метод addDate в файле weatherParser/views
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)) # Нужно для иконки во вкладке
]