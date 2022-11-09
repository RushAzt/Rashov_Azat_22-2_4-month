from django.shortcuts import render, HttpResponse
import datetime

def main(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')

def date_now(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())

def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
# Create your views here.
