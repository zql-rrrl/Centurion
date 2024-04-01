from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Maxim

# Create your views here.
def test(request):
    maxim = Maxim.objects.all()
    json = [{'author': say.author, 'quote': say.quote} for say in maxim]
    return JsonResponse(json, safe=False)

