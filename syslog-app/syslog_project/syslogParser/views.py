from django.shortcuts import render
from django.http import HttpResponse
from .Classes import classFiles # Импортируем файл files.py
#from django.http import JsonResponse

# Create your views here.
def index(request):
    if (request.method == 'GET'):
        print('OK')
    return render(request, 'syslogParser/index.html')
#
# def getData(request):
#     if (request.method == 'GET'):
#         syslog_lst = []
#         file = classFiles.File(classFiles.path) # Экземпляр класса File из выйла files.py
#         for elem in file.readFile(): # Метод readFile()
#             syslog_lst.append(elem)
#     return HttpResponse(syslog_lst)
#
def serchData(request, serchString):
    if (request.method == 'GET'):
        context = {'syslog':[]}
        file = classFiles.File(classFiles.path)  # Экземпляр класса File из выйла files.py
        for elem in file.readFile():
            if file.findSymbols(elem, serchString):
                context['syslog'].append(elem)
            else: continue
    return HttpResponse(context['syslog'])
#
def serchDataAll(request, indexArray = 0):
    if (request.method == 'GET'):
        context = {'syslog': []}
        file = classFiles.File(classFiles.path)  # Экземпляр класса File из выйла files.py
        for elem in file.readFile():  # Метод readFile()
                 context['syslog'].append(elem)
    return HttpResponse(context['syslog'])

