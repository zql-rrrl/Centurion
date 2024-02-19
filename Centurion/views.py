from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME')


def one(request):
    return HttpResponse('ONE')

