# Generated by Django 4.2.9 on 2024-02-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_email_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=320, unique=True, verbose_name="Email Address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=94, verbose_name="Password"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=64, unique=True, verbose_name="Username"),
        ),
    ]
