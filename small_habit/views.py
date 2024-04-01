from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import EveryDay

# Create your views here.
def test(request):
    return HttpResponse('SMALL HABIT TEST')


def get_habit(request):
    habit_list = EveryDay.objects.filter(state=False, categorize='CAT1')
    habit_json = [{
        'id': habit.id,
        'habit': habit.habit,
        'state': habit.state,
        'sort': habit.sort,
    } for habit in habit_list]
    print(habit_json)
    return JsonResponse(habit_json, safe=False)


