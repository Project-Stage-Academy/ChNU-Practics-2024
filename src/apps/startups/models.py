import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

from apps.users.models import User


# from pictures.models import PictureField


class Startup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField("Company Name", max_length=64)

    STARTUP_SIZE = (("S", "Small"), ("M", "Medium"), ("B", "Big"), ("L", "Large"))

    size = models.CharField(
        max_length=1,
        choices=STARTUP_SIZE,
        blank=True,
        default="S",
        help_text="Startup size",
    )

    phone_number = models.CharField(
        max_length=16,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r"^[\+]?[(]?[0-9]{3}[)]?[\s\.]?[0-9]{3}[\s\.]?[0-9]{4,6}$",
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.",
            ),
        ],
    )

    location = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField("Created", default=timezone.now)
    #    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


class StartupFounder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, related_name="investor", null=True
    )
    is_active = models.BooleanField(default=True)
    startup_id = models.ForeignKey(
        Startup, on_delete=models.SET_NULL, related_name="founders", null=True
    )

    def __str__(self):
        return str(self.user)
