from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Advisor(models.Model):
    name = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(2,"Enter two or more characters")]
    )
    url = models.URLField(max_length=10000)


class Meetings(models.Model):
    advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
