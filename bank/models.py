from django.db import models

# Create your models here.
class Branch(models.Model):
  count = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)