from django.contrib import admin
from django.utils.html import format_html
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'uploaded_at', 'file_link')
    readonly_fields = ('file_link',)

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">Download</a>', obj.file.url)
        return "-"
    file_link.short_description = "Resume"
