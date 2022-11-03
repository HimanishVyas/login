from django.db import models
from django.contrib.auth.models import User
# from  django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.
class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Tasktitle = models.CharField(max_length=70)
    Taskdesc = models.CharField(max_length=1000)


def __str__(self):
        return self.Tasktitle