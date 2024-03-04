# Generated by Django 4.2.10 on 2024-02-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0011_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("investor", "Investor"),
                    ("startup", "Startup"),
                    ("both", "Both"),
                ],
                default="both",
                max_length=10,
            ),
        ),
    ]