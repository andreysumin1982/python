from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if (request.method == 'GET'):
        print('ok')
    return render(request, 'syslogParser/index.html')