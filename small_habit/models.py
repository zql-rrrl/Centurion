from django.db import models

# Create your models here.
class EveryDay(models.Model):
    # 定义一个选择类，用于分类字段
    CATEGORY_CHOICES = [
        ('CAT1', '一定要'),
        ('CAT2', '自定义'),
        ('CAT3', '其他'),
    ]

    sort = models.PositiveSmallIntegerField(default=100)  # 优先级
    habit = models.CharField(max_length=255, null=False, blank=False)  # 习惯
    state = models.BooleanField(default=False)  # 状态
    principle = models.TextField(null=True, blank=True)  # 原理
    img = models.URLField(null=True, blank=True)  # 图片
    categorize = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default='CAT1')  # 归类

    def __str__(self):
        return self.habit

