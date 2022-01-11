from django.views.generic import RedirectView
from django.urls import path
#from django.conf.urls import url
# Импортируем views из папки приложения weatherParser
from django.conf.urls.static import static
from .import views
#
urlpatterns = [
    path('', views.index, name='index'),# метод index в файле weatherParser/views
    path('json/', views.getJson, name='json'),# метод getJson в файле weatherParser/views
    path('summary/', views.showSummary, name='summary'),  # метод showSummary в файле weatherParser/views
    path('add/', views.addData, name='add'),# метод addDate в файле weatherParser/views
    path('summary_date/<str:str1>/<str:str2>/', views.showSummaryDate, name='summary_date'),# метод delTable в файле weatherParser/views
    #url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)) # Нужно для иконки во вкладке
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)) # Нужно для иконки во вкладке
]