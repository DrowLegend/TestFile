from django.db import models
from django.contrib.auth.models import User
from .tasks import set_status_as_inactive

# Create your models here.


class UploadFile(models.Model):
    file = models.FileField()
    is_active = models.BooleanField(default='False')




