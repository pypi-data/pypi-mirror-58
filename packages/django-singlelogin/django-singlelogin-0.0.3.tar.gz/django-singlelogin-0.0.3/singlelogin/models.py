from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Visitor(models.Model):
    pupil = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    session_key = models.CharField(null=False, max_length=40)
