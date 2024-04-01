from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    sequence = models.PositiveIntegerField(unique=True, blank=False, null=False)  # 序号
    word = models.CharField(max_length=50, blank=False, null=False)  # 词汇
    part_of_speech = models.CharField(max_length=10, blank=False, null=False)  # 词性
    collins_star = models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], blank=False, null=False, default=0)
    meaning = models.CharField(max_length=255, blank=True, null=True)  # 含义
    prefix = models.CharField(max_length=50, blank=True, null=True)  # 前缀
    root = models.CharField(max_length=50, blank=True, null=True)  # 词根
    suffix = models.CharField(max_length=50, blank=True, null=True)  # 后缀

    def __str__(self):
        return self.word



