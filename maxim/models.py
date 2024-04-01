from django.db import models

# Create your models here.
class Maxim(models.Model):
    author = models.CharField('智者', max_length=200, blank=True)
    quote = models.CharField('名言', max_length=500, blank=False, default='四大皆空')
    importance = models.IntegerField(default=1, choices=[(1, '常规'), (2, '重要'), (3, '非常重要')])

    def __str__(self):
        return f"{self.quote} - {self.author}"

