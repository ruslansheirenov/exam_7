from django.contrib import admin

# Register your models here.

from .models import Poll, Choice

class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    search_fields = ['question']
    fields = ['question', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)