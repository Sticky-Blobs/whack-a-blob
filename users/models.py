from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from helpers.models import BaseModel


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, address, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(address, **other_fields)

    def create_user(self,address, **other_fields):

        user = self.model(address=address,**other_fields)
        user.save()
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    address = models.CharField(max_length=150, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'address'
    
    def __str__(self):
        return self.address