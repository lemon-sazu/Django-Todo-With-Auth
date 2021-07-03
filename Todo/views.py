from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def taskList(request):
    return HttpResponse('To Do List')
