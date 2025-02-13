from django.contrib import admin
from .models import PortfolioItem1
from django.utils.html import format_html

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'project_title')
    readonly_fields = ('thumbnail_preview', 'modal_image_preview')

    def thumbnail_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px;"/>', obj.thumbnail.url) if obj.thumbnail else ''
    
    def modal_image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px;"/>', obj.modal_image.url) if obj.modal_image else ''

    thumbnail_preview.short_description = 'Thumbnail Preview'
    modal_image_preview.short_description = 'Modal Image Preview'

    fieldsets = (
        ('Portfolio Item', {
            'fields': ('title', 'subtitle', 'thumbnail', 'thumbnail_preview')
        }),
        ('Modal Content', {
            'fields': ('modal_id', 'project_title', 'intro_text', 
                      'modal_image', 'modal_image_preview',
                      'description', 'client', 'category')
        }),
    )

admin.site.register(PortfolioItem1, PortfolioAdmin)