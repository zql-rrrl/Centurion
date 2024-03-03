from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Maxim

# Create your views here.
def one(request):
    return HttpResponse('Maxim One')


def two(request):
    return HttpResponse('Maxim Two')


def three(request):
    maxim = Maxim.objects.all()
    json = [{'author': say.author, 'quote': say.quote} for say in maxim]
    return JsonResponse(json, safe=False)

