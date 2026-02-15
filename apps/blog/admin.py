from django.contrib import admin
from .models import Group_blog, Author, Blog,Lable_blog,Comment,Meta_tag_model

# تنظیم پنل ادمین برای مدل Group_blog
@admin.register(Group_blog)
class GroupBlogAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('group_name',)
    ordering = ('group_name',)

# تنظیم پنل ادمین برای مدل Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Author_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('Author_name',)
    ordering = ('Author_name',)


class LableBlogInline(admin.TabularInline):
    model = Lable_blog


class BlogMetaAdminInlin(admin.TabularInline):
    model = Meta_tag_model
    extra = 1

# تنظیم پنل ادمین برای مدل Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name_blog', 'subject', 'grop_blog', 'view', 'is_active', 'time_read', 'register_data', 'update_data')
    list_filter = ('grop_blog', 'is_active', 'register_data')
    search_fields = ('name_blog', 'subject', 'grop_blog__group_name', 'Auther_blog__Author')
    ordering = ('-register_data',)
    filter_horizontal = ('Auther_blog',)
    inlines = [LableBlogInline,BlogMetaAdminInlin]

    # تنظیم فیلدهای قابل ویرایش در صفحه اصلی
    list_editable = ('is_active', 'view')


    # تنظیم ظاهر فرم
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name_blog', 'subject', 'grop_blog', 'Auther_blog', 'image_name', 'view', 'is_active', 'time_read', 'slug','city_link',)
        }),
        ('توضیحات', {
            'fields': ('description', 'description2')
        }),
        ('تاریخ‌ها', {
            'fields': ('register_data', 'update_data')
        }),
    )

    # جلوگیری از ویرایش تاریخ‌ها در فرم
    readonly_fields = ('register_data', 'update_data')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('full_name','text','blog','is_active',)
    list_editable = ['is_active']