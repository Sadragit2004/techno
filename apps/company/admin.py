from django.contrib import admin
from .models import Company_Information, Resum_Company,Social_Media



class ResumCompanyAdminInline(admin.TabularInline):
    model = Resum_Company
    extra = 1


class SocialCompanyAdminInline(admin.TabularInline):
    model = Social_Media
    extra = 1




@admin.register(Company_Information)
class CompanyInformationAdmin(admin.ModelAdmin):
    """Admin customization for Company_Information."""
    list_display = ('name_company', 'phone_number', 'mobile_number', 'email','video',)
    search_fields = ('name_company', 'email', 'phone_number', 'mobile_number')
    list_filter = ('name_company',)
    ordering = ('name_company',)
    inlines = [ResumCompanyAdminInline,SocialCompanyAdminInline]
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name_company', 'phone_number', 'mobile_number', 'email'),
        }),
        ('آدرس و تصویر', {
            'fields': ('address', 'address_link', 'image_name','video'),
        }),
    )


@admin.register(Resum_Company)
class ResumCompanyAdmin(admin.ModelAdmin):
    """Admin customization for Resum_Company."""
    list_display = ('subject', 'company', 'title_subject', 'register_date', 'is_active')
    list_filter = ('is_active', 'register_date',)
    search_fields = ('subject', 'decription', 'title_subject')
    ordering = ('-register_date',)
    list_editable = ('is_active',)
   
    fieldsets = (
        ('اطلاعات رزومه', {
            'fields': ('company', 'subject', 'decription', 'title_subject'),
        }),
        ('تاریخ‌ها و وضعیت', {
            'fields': ('register_date', 'is_active'),
        }),
        ('تصویر رزومه', {
            'fields': ('image_name',),
        }),
    )

