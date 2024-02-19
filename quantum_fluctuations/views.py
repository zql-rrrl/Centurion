from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def one(request):
    return HttpResponse('QF one')


def two(request):
    return HttpResponse('QF two')

