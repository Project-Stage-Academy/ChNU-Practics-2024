import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

from apps.users.models import Founder, User


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField("Project Name", max_length=64)
    PROJECT_TYPE = (("P", "Project"), ("I", "Idea"))

    project_type = models.CharField(
        max_length=1,
        choices=PROJECT_TYPE,
        blank=True,
        default="P",
        help_text="Project type",
    )
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField("Description", max_length=500, blank=True, null=True)
    media_url = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return self.project_name


class Startup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField("Company Name", max_length=64)
    bio = models.TextField("Bio", max_length=500, blank=True, null=True)

    founders = models.ManyToManyField(Founder)
    projects = models.ManyToManyField(Project)

    STARTUP_SIZE = (("S", "Small"), ("M", "Medium"), ("B", "Big"), ("L", "Large"))

    size = models.CharField(
        max_length=1,
        choices=STARTUP_SIZE,
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

    location = models.CharField(max_length=255, blank=True)


    created_at = models.DateTimeField("Created", default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name
