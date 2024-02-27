from django.contrib import admin

from .models import Project, Startup


admin.site.register(Startup)
admin.site.register(Project)
