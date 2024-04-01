from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class MainCategory(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    sort = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], null=True)

    def __str__(self):
        return self.title


class Tools(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    sort = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], null=True)
    origin = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Modules(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    sort = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], null=True)
    origin = models.ForeignKey(Tools, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.TextField(blank=True)
    img = models.URLField(max_length=1024, blank=True)
    proficiency = models.IntegerField(choices=[(0, '未知'), (1, '初学者'), (2, '了解'), (3, '熟练'), (4, '专家')])
    set_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    responsive = models.TextField(blank=True)
    res_mode = models.IntegerField(choices=[(0, '思考'), (1, '单行文本'), (2, '单行代码'), (3, '多行文本'), (4, '多行代码')])
    sort = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], null=True)
    origin = models.ForeignKey(Modules, on_delete=models.CASCADE)
