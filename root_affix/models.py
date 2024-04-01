from django.db import models

# Create your models here.

# 词根表
class Root(models.Model):
    FREQUENCY_CHOICES = [
        ('VERY_HIGH', 'Very High'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    ORIGIN_CHOICES = [
        ('LATIN', 'Latin'),  # 拉丁语
        ('GREEK', 'Greek'),  # 希腊语
        ('FRENCH', 'French'),  # 法语
        ('OLD_ENGLISH', 'Old English'),  # 古英语
        ('GERMAN', 'German'),  # 德语
        ('ITALIAN', 'Italian'),  # 意大利语
        ('OTHER', 'Other'),  # 其他语言
    ]

    root = models.CharField(max_length=50)  # 词根
    meaning = models.CharField(max_length=255)  # 含义
    origin = models.CharField(max_length=100, choices=ORIGIN_CHOICES, blank=True, null=True)  # 来源
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, default='LOW')  # 频率
    image_url = models.URLField(blank=True, null=True)  # 图片地址
    story = models.TextField(blank=True, null=True)  # 背后的故事

    def __str__(self):
        return self.root


# 词目表
class Word(models.Model):
    root = models.ForeignKey(Root, on_delete=models.CASCADE, related_name='words')
    term = models.CharField(max_length=255)  # 词条
    meaning = models.CharField(max_length=255)  # 含义


# 词族表
class Family(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='families')
    term = models.CharField(max_length=255)  # 词条
    meaning = models.CharField(max_length=255)  # 含义


# 前缀表
class Prefix(models.Model):
    FREQUENCY_CHOICES = [
        ('VERY_HIGH', 'Very High'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    ORIGIN_CHOICES = [
        ('LATIN', 'Latin'),  # 拉丁语
        ('GREEK', 'Greek'),  # 希腊语
        ('FRENCH', 'French'),  # 法语
        ('OLD_ENGLISH', 'Old English'),  # 古英语
        ('GERMAN', 'German'),  # 德语
        ('ITALIAN', 'Italian'),  # 意大利语
        ('OTHER', 'Other'),  # 其他语言
    ]

    prefix = models.CharField(max_length=255, unique=True)  # 前缀
    meaning = models.TextField()  # 含义
    origin = models.CharField(max_length=100, choices=ORIGIN_CHOICES, blank=True, null=True)  # 来源
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, default='LOW')  # 频率
    image_url = models.URLField(blank=True, null=True)  # 图片地址
    story = models.TextField(blank=True, null=True)  # 背后的故事


# 前缀词汇表
class PrefixVocabulary(models.Model):
    prefix = models.ForeignKey(Prefix, on_delete=models.CASCADE, related_name='vocabulary')
    term = models.CharField(max_length=255)  # 词条
    meaning = models.CharField(max_length=255)  # 含义


# 后缀表
class Suffix(models.Model):
    FREQUENCY_CHOICES = [
        ('VERY_HIGH', 'Very High'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    ORIGIN_CHOICES = [
        ('LATIN', 'Latin'),  # 拉丁语
        ('GREEK', 'Greek'),  # 希腊语
        ('FRENCH', 'French'),  # 法语
        ('OLD_ENGLISH', 'Old English'),  # 古英语
        ('GERMAN', 'German'),  # 德语
        ('ITALIAN', 'Italian'),  # 意大利语
        ('OTHER', 'Other'),  # 其他语言
    ]

    suffix = models.CharField(max_length=255, unique=True)  # 后缀
    meaning = models.CharField(max_length=255)  # 含义
    origin = models.CharField(max_length=100, choices=ORIGIN_CHOICES, blank=True, null=True)  # 来源
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, default='LOW')  # 频率
    image_url = models.URLField(blank=True, null=True)  # 图片地址
    story = models.TextField(blank=True, null=True)  # 背后的故事


# 后缀词汇表
class SuffixVocabulary(models.Model):
    suffix = models.ForeignKey(Suffix, on_delete=models.CASCADE, related_name='vocabulary')
    term = models.CharField(max_length=255)  # 词条
    meaning = models.CharField(max_length=255)  # 含义

