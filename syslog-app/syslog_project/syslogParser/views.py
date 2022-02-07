from django.shortcuts import render
from django.http import HttpResponse
from .Classes import files
from django.http import JsonResponse

# Create your views here.
def index(request):
    if (request.method == 'GET'):
        print('ok')
    return render(request, 'syslogParser/index.html')
#
def getData(request):
    if (request.method == 'GET'):
        context = {'syslog':[]}
        lst = []
        file = files.File(files.path)
        for elem in file.readFile():
            lst.append(elem)

        print(lst)
    return HttpResponse(lst)