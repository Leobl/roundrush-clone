from django.shortcuts import render
from django.http import HttpResponse

def issues(request):
    return HttpResponse('Issues')
