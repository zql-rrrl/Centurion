from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # 用户基本信息
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    # 0为免费用户，数字越大，等级越高
    subscription_level = models.IntegerField(default=0)

    # 国家、省份、城市
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    # 社交媒体链接
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)

    # 生日
    date_of_birth = models.DateField(null=True, blank=True)

    # 用户状态：邮件是否验证、账户是否被禁用等
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # 加入日期和最后登录时间
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
