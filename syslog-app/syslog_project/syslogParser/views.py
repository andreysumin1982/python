from django.shortcuts import render
from django.http import HttpResponse
from .Classes import classFiles # Импортируем файл classFiles.py
#from django.http import JsonResponse

# Create your views here.
def index(request):
    if (request.method == 'GET'):
        pass
    return render(request, 'syslogParser/index.html')
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
        file = classFiles.File(classFiles.path)  # Экземпляр класса File из фыйла files.py
        for elem in file.readFile():  # Метод readFile()
            context['syslog'].append(elem)
    return HttpResponse(context['syslog'])
#
def serchZipFiles(request):
    if (request.method == 'GET'):
        #context = {'zipFiles':[]}
        file = classFiles.File(classFiles.pathZipFiles) # Экземпляр класса File из фыйла files.py  
    return HttpResponse(file.readZipFiles())
#
def extractZipFile(request, zipFile):
    if (request.method == 'GET'):
        context = {'syslog': []}
        file = classFiles.File(zipFile) # Экземпляр класса File из фыйла files.py
        path = file.extractZip()
        file2 = classFiles.File(path) # Экземпляр класса File2 c абсолютным путем распак.файла
        for elem in file2.readFile():  # Метод readFile()
            context['syslog'].append(elem)
    return HttpResponse(context['syslog'])
#
def serchZipData(request, zipFile, serchString):
    if (request.method == 'GET'):
        context = {'syslog': []}
        file = classFiles.File(zipFile) # Экземпляр класса File из фыйла files.py
        path = file.extractZip()
        file2 = classFiles.File(path) # Экземпляр класса File2 c абсолютным путем распак.файла
        for elem in file2.readFile():  # Метод readFile()
            if file2.findSymbols(elem, serchString):
                context['syslog'].append(elem)
            else: continue
    return HttpResponse(context['syslog'])
#