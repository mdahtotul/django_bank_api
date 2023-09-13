from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_A = "admin"
ROLE_M = "manager"
ROLE_O = "officer"
ROLE_C = "cashier"
ROLE_U = "user"

ROLE_TYPES = [
    (ROLE_U, "user"),
    (ROLE_C, "cashier"),
    (ROLE_O, "officer"),
    (ROLE_M, "manager"),
    (ROLE_A, "admin"),
]


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    role = models.CharField(max_length=10, choices=ROLE_TYPES, default=ROLE_U)
