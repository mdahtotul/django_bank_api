from django.db import models
from django.conf import settings

from bank.constants import ACC_CURRENT, ACC_TYPES

class Address(models.Model):
  details = models.CharField(max_length=500, null=True, blank=True)
  state = models.CharField(max_length=100, null=True, blank=True)
  zip_code = models.CharField(max_length=100, null=True, blank=True)
  city = models.CharField(max_length=100)
  country = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.details}, {self.city}, {self.country}"


class Bank(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=100, null=True, blank=True)


class Branch(models.Model):
  name = models.CharField(max_length=255)
  routing_no = models.CharField(max_length=255, null=True, blank=True)
  address = models.OneToOneField(Address, on_delete=models.PROTECT, blank=True, null=True)
  phone = models.CharField(max_length=15, null=True, blank=True)


class Account(models.Model):
  UNO = models.CharField(max_length=20)
  type = models.CharField(max_length=10, choices=ACC_TYPES, default=ACC_CURRENT)
  phone = models.CharField(max_length=15, null=True, blank=True)
  bod = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
  balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

  user = models.ForeignKey(settings.AUTH_USER_MODEL,
   on_delete=models.CASCADE, related_name="accounts")
  branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name="accounts")
  address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="accounts")

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)