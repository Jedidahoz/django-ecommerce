from django.contrib import admin
from userauths.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'bio']

admin.site.register(CustomUser, CustomUserAdmin)