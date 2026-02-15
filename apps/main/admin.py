from django.contrib import admin

from .models import Main_Slider,GalleryMain

class GalleryMainSlider(admin.TabularInline):
    model = GalleryMain
    extra = 1



@admin.register(Main_Slider)
class MainSlider(admin.ModelAdmin):

    list_display = ('title',)
    inlines = [GalleryMainSlider]