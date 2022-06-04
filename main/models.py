from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Lesson(models.Model):
    topic = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    isPassed = models.BooleanField(default=False)
    dataPassed = models.DateTimeField(blank=True, null=True)