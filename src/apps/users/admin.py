from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Founder, Investor, User


admin.site.register(User, UserAdmin)
admin.site.register(Founder)
admin.site.register(Investor)
