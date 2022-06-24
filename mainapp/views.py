from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .tasks import test_func

# Create your views here.
def test(request):
    test_func.delay()   #invoke the task function using the delay() function
    return HttpResponse("Done")





