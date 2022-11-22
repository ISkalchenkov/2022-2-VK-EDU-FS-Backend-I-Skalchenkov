from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email','is_superuser',)
    list_filter = ('is_superuser', 'is_active', 'is_staff',)
    search_fields = ('username', 'first_name', 'last_name',)


admin.site.register(User, UserAdmin)
