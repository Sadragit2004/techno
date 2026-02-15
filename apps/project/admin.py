from django.contrib import admin
from .models import Meta_tag_model,MemeberCompany,GroupProject,Project,ProjectFeature,Feature,FeatureValue,project_Gallery

# Register your models here.

@admin.register(GroupProject)
class GroupProjectAdmin(admin.ModelAdmin):

    list_display = ('title',)


class FeatureValueInline(admin.TabularInline):
    model = FeatureValue
    extra = 1




@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature_name',)
    list_filter = ('feature_name',)
    search_fields = ('feature_name',)
    ordering = ('feature_name',)
    inlines = [FeatureValueInline]



class ProjectGalleryInline(admin.TabularInline):
    model = project_Gallery


class projectFeatureAdmin(admin.TabularInline):
    model = ProjectFeature
    extra = 1


class MetaTagmdelService(admin.TabularInline):
    model = Meta_tag_model
    extra = 1



class MetaTagmdelProject(admin.TabularInline):
    model = Meta_tag_model
    extra = 1




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title',)
    inlines = [projectFeatureAdmin,ProjectGalleryInline,MetaTagmdelProject]




@admin.register(MemeberCompany)
class MemberCompanyAdmin(admin.ModelAdmin):

    list_display = ('full_name',)