# Generated by Django 4.2.10 on 2024-02-20 10:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=64, verbose_name='Company Name')),
                ('size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('B', 'Big'), ('L', 'Large')], default='S', help_text='Startup size', max_length=1)),
                ('phone_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='^[\\+]?[(]?[0-9]{3}[)]?[\\s\\.]?[0-9]{3}[\\s\\.]?[0-9]{4,6}$')])),
                ('location', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StartupFounder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('startup_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='founders', to='startups.startup')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]