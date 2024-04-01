from django.http import HttpResponse
from django.shortcuts import render
from .models import Vocabulary
import openpyxl
import os

# Create your views here.
def test(request):
    return HttpResponse('HIGH TEST')


def add_word(request):
    file_path = os.path.join(os.path.dirname(__file__), '20000.xlsx')

    # 使用openpyxl读取Excel文件
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    # 读取数据并写入数据库
    for row in sheet.iter_rows(min_row=2, values_only=True):
        collins_star = row[3] if row[3] is not None else 0

        Vocabulary.objects.create(
            sequence=row[0],
            word=row[1],
            part_of_speech=row[2],
            collins_star=collins_star,
            meaning=row[5],
            prefix='',
            root='',
            suffix='',
        )

    return HttpResponse('ADD WORD')


def set_cx(request):
    Vocabulary.objects.filter(part_of_speech='p').update(part_of_speech='pron.')
    return HttpResponse('SET CX')


def get_word(request):
    words = Vocabulary.objects.values('word')
    s = ''
    for word in words:
        s = s + word['word'] + ', '

    return HttpResponse(s)
