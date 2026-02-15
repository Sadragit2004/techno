from django.contrib import admin
from .models import *

# پنل ادمین برای GroupService
@admin.register(GroupService)
class GroupServiceAdmin(admin.ModelAdmin):
    list_display = ('title_group', 'is_active', 'register_date', 'update_date')
    list_filter = ('is_active', 'register_date')
    search_fields = ('title_group',)
    ordering = ('-register_date',)

class MetaTagmdelService(admin.TabularInline):
    model = Meta_tag_model
    extra = 1

# پنل ادمین برای Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'group_service', 'is_active', 'register_date', 'update_date')
    list_filter = ('is_active', 'group_service', 'register_date')
    search_fields = ('title', 'summery')
    ordering = ('-register_date',)
    autocomplete_fields = ('group_service',)
    readonly_fields = ('register_date', 'update_date')
    inlines = [MetaTagmdelService]


# پنل ادمین برای Service_Gallery
@admin.register(Service_Gallery)
class ServiceGalleryAdmin(admin.ModelAdmin):
    list_display = ('Serviceice', 'is_active', 'image_name')
    list_filter = ('is_active', 'Serviceice')
    search_fields = ('Serviceice__title',)
    ordering = ('Serviceice',)
