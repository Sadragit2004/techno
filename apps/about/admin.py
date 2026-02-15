from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(About_us)
class AdminAbout(admin.ModelAdmin):

    list_display = ('title',)


@admin.register(ManyQuestion)
class ManyQuestion(admin.ModelAdmin):
    list_display = ('question','answer',)