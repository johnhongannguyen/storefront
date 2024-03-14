from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
# request - response


def calculate():
    x = 2
    y = 1
    return x


def say_hello(request):
    x = calculate()

    return render(request, 'hello.html')
