from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.


def index(request):
    return render_to_response('SS/index.html')


def tos(request):
    return render_to_response('SS/tos.html')


def order(request):
    return render_to_response('SS/index.html')
