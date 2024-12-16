from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user', 'fullname', 'initials', 'initialsColor')
    search_fields = ('fullname', 'initials')
