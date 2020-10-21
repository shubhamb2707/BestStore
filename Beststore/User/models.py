from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import *
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
