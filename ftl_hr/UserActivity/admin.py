from django.contrib import admin
from .models import User,ActivityPeriod

# Registering my User model for Admin Panel
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','real_name','tz']

# Registering my ActivityPeriod model for Admin Panel
@admin.register(ActivityPeriod)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_id','start_time','end_time']