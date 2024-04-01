from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from accounts.models import Profile
from faker import Faker

# Create your views here.
def add_user(request):
    fake = Faker()
    user_count = 20  # 或者根据请求参数来设定生成的用户数量

    for _ in range(user_count):
        # 创建 User
        username = fake.user_name()
        email = fake.email()
        password = "testpassword"  # 在实际应用中，密码应更复杂且随机
        user = User.objects.create_user(username=username, email=email, password=password)

        # 创建 Profile
        Profile.objects.create(
            user=user,
            phone_number=fake.phone_number(),
            bio=fake.text(),
            country=fake.country(),
            state=fake.state(),
            city=fake.city(),
            linkedin=fake.url(),
            twitter=fake.url(),
            github=fake.url(),
            date_of_birth=fake.date_of_birth(),
            email_verified=fake.boolean(),
            is_active=fake.boolean()
        )

    return HttpResponse(f"Successfully added {user_count} fake users.")


