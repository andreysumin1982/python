from django.shortcuts import render
from django.http import HttpResponse
from .Classes import files # Импортируем файл files.py
from django.http import JsonResponse

# Create your views here.
def index(request):
    if (request.method == 'GET'):
        print('ok')
    return render(request, 'syslogParser/index.html')
#
def getData(request):
    if (request.method == 'GET'):
        syslog_lst = []
        file = files.File(files.path) # Экземпляр класса File из выйла files.py
        for elem in file.readFile(): # Метод readFile()
            syslog_lst.append(elem)
    return HttpResponse(syslog_lst)