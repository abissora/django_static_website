from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# return HttpResponse('<h1>this is my homepage</h1>
def hi(request):
    return render(request, 'proj2/hi.html')


def h2(request):

    return render(request, 'proj2/h2.html')


def h3(request):
    return render(request, 'proj2/h3.html')


def h4(request):
    return render(request, 'proj2/h4.html')
