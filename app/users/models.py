from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class Position(models.Model):
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(_("username"), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    position = models.ForeignKey(
        Position,
        related_name='users',
        on_delete=models.CASCADE,
        null=True
    )
    rate = models.FloatField(blank=True, null=True)
    department = models.ForeignKey(
        'Department',
        related_name='users',
        null=True,
        on_delete=models.CASCADE,
    )
    employee_code = models.IntegerField(blank=True, null=True, unique=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Department(models.Model):
    name = models.CharField(max_length=200, blank=True)
    manager = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class WorkingHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    hours = models.FloatField(blank=True)
    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.user} - {self.date}"



class Payouts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    begin_date_interval = models.DateField(blank=True)
    end_date_interval = models.DateField(blank=True)
    amount = models.FloatField(blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    @property
    def total_amount(self):
        total_amount = self.amount
        if hasattr(self, 'bonuses_amount') and self.bonuses_amount:
            total_amount += self.bonuses_amount
        return total_amount


class Bonus(models.Model):
    payout = models.ForeignKey(
        Payouts,
        related_name='bonuses',
        on_delete=models.CASCADE,
    )
    amount = models.FloatField(blank=True)
    description = models.TextField(blank=True)


