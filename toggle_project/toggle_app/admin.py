from django.contrib import admin
from .models import ToggleItem

class ToggleItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')  # Display these fields in the admin list view
    list_filter = ('is_active',)         # Add filter by 'is_active'
    search_fields = ('name',)            # Add search by 'name'
    list_editable = ('is_active',)       # Allow editing 'is_active' directly in the list view

admin.site.register(ToggleItem, ToggleItemAdmin)
