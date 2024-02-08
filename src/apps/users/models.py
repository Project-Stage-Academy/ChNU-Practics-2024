import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserRole(models.TextChoices):
    INVESTOR = "investor", "Investor"
    STARTUP = "startup", "Startup"


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        password: str | None = None,
        role: UserRole | None = None,
        **extra_fields,
    ) -> "User":
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField("Role", max_length=8, choices=UserRole.choices)
    username = models.CharField(
        "Username", max_length=64, unique=True, blank=False, null=False
    )
    password = models.CharField("Password", max_length=94, blank=False, null=False)
    email = models.EmailField(
        "Email Address", max_length=320, unique=True, blank=False, null=False
    )

    first_name = models.CharField("First Name", max_length=15, blank=True, null=True)
    last_name = models.CharField("Last Name", max_length=15, blank=True, null=True)

    objects: CustomUserManager = CustomUserManager()

    class Meta:
        verbose_name_plural = "users"
        ordering = ["email"]
        indexes = [models.Index(fields=["email"])]

    def __str__(self) -> str:
        return self.email

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
