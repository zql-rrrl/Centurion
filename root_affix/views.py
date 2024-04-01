from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import os
import random
from .models import Root, Prefix, Suffix

# Create your views here.
def test(request):
    return HttpResponse('ROOT_Affix')


def very_high_root(request):
    roots = Root.objects.filter(frequency='VERY_HIGH')
    roots_json = [
        {
            'id': root.id,
            'root': root.root,
            'meaning': root.meaning,
            'origin': root.origin,
            'story': root.story,
            'img': root.image_url
        } for root in roots
    ]
    random.shuffle(roots_json)
    return JsonResponse(roots_json, safe=False)




