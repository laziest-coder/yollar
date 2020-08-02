import random
import string

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserProfileManager(BaseUserManager):
    def create_user(self, device_id=None, username=None, password=None):
        if not device_id:
            device_id = self.generate_random_device_id()
            # raise ValueError('Users must have device id.')

        user = self.model(
            device_id=device_id,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, password=None):
        user = self.create_user(
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    @staticmethod
    def generate_random_device_id(size=16, chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


class UserProfile(AbstractBaseUser):
    device_id = models.CharField(max_length=16)
    username = models.CharField(blank=True, unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.device_id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        unique_together = ('device_id', 'username')
