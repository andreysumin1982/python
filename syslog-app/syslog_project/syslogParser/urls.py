from django.views.generic import RedirectView
from django.urls import path
#from django.conf.urls import url
# Импортируем views из папки приложения syslogParser
from django.conf.urls.static import static
from .import views
 
urlpatterns =[
    path('', views.index, name='index'),  # метод index в файле syslogParser/views
    #path('add/', views.addData, name='add'),  # метод addDate в файле syslogParser/views
    #path('getData/', views.getData, name='getData'),  # метод getData в файле syslogParser/views
    path('serchDataAll/', views.serchDataAll, name='serchDataAll'),
    path('serchData/<str:serchString>/', views.serchData, name='serchData'),  # метод serchData в файле syslogParser/views
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)) # Нужно для иконки во вкладке
]
