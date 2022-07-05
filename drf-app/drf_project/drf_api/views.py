import random
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import encodeTest
from .serializers import encodeTest2
# Create your views here.

#
def index(request):
    if (request.method == 'GET'):
        return render(request, 'drf_api/index.html')
#
def testApi(request):
    if (request.method == 'GET'):
        return HttpResponse(encodeTest(), content_type='application/json')
#
def testApi2(request):
    if (request.method == 'GET'):
        arrlist = [random.randint(1,1000) for j in range(random.randrange(1000))]
        return HttpResponse(encodeTest2(random.randrange(100), arrlist), content_type='application/json')