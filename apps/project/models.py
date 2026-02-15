from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import funcs
from django.utils import timezone
# Create your models here.

class GroupProject(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان پروزه')
    is_active = models.BooleanField(default=True)
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')
    update_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ اپدیت')



    def __str__(self) -> str:
        return self.title



class Feature(models.Model):
    feature_name = models.CharField(max_length=100,verbose_name='نام ویژگی')
    Project_group = models.ManyToManyField(GroupProject,verbose_name='گروه پروژه',related_name='features_of_group')



    def __str__(self) -> str:
        return f'{self.feature_name}'

class Project(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان خدمات',)
    summery = models.TextField(verbose_name='توضیح کوتاه')
    decription = RichTextUploadingField(verbose_name='2توضیحات',config_name = 'special',blank = True,null=True)
    image_file = funcs.FileUpload('img','service_img')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='ادرس عکس')
    group_service = models.ForeignKey(GroupProject,on_delete=models.CASCADE,verbose_name='گروه سرویس ها',related_name='Group_Project')
    slug = models.CharField(max_length=50,verbose_name='اسلاگ',null=True,blank=True)
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')
    update_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ اپدیت')
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    features = models.ManyToManyField(Feature,through='projectfeature')


    def __str__(self) -> str:
        return f'{self.title}'



    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'




class Meta_tag_model(models.Model):
    projedct = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='project_meta', null=True, blank=True
    )
    page_title = models.CharField(max_length=255, null=True, blank=True)  # عنوان صفحه
    description = models.TextField(null=True, blank=True)  # توضیحات، حداکثر 128 کاراکتر
    og_title = models.CharField(max_length=255, null=True, blank=True)  # عنوان OG
    og_description = models.TextField(null=True, blank=True)  # توضیحات OG
    og_image = models.URLField(null=True, blank=True)  # تصویر OG (URL)

    # این فیلد برای مدیریت ساختار og (Open Graph)
    og_url = models.URLField(null=True, blank=True)  # URL برای OG
    og_type = models.CharField(max_length=50, null=True, blank=True)  # نوع محتوای OG (مثلاً article یا website)

    # برای تعیین تاریخ و زمان ایجاد و آپدیت
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_title or 'Meta Tag for {}'.format(self.service)

    def save(self, *args, **kwargs):
        # اگر توضیحات بیش از 128 کاراکتر باشد، آنها را کوتاه می‌کنیم
        if self.description and len(self.description) > 128:
            self.description = self.description[:128]
        super(Meta_tag_model, self).save(*args, **kwargs)





class FeatureValue(models.Model):
    value_title = models.CharField(max_length=100,verbose_name='عنوان مقدار')
    feature = models.ForeignKey(Feature,on_delete=models.CASCADE,verbose_name='ویژگی',null=True,blank=True,related_name='feature_value')
    english_value = models.CharField(max_length=20,verbose_name='مقدار انگلیسی',null=True,blank=True)


    def __str__(self) -> str:
        return self.value_title

#=======================================================

class ProjectFeature(models.Model):
    project_s = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='پروژه',related_name='features_value')
    feature = models.ForeignKey(Feature,verbose_name='ویژگی',on_delete=models.CASCADE)
    value = models.CharField(max_length=40,verbose_name='مقدار پروژه')
    english = models.CharField(verbose_name='انگلیسی',max_length=20,blank=True,null=True)
    filter_value = models.ForeignKey(FeatureValue,null=True,blank=True,on_delete=models.CASCADE,verbose_name='فیلترینگ مقدار')


    def __str__(self) -> str:
        return f'{self.feature}\t{self.project_s}\t{self.value}'


    class Meta:
        verbose_name = 'ویژگی پروژه ها'
        verbose_name_plural = 'ویژگی های پروژه ها'






class project_Gallery(models.Model):
    product = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='کالا',related_name='gallery_project')
    file_upload = funcs.FileUpload('images','project_gallery_img')
    image_name = models.ImageField(upload_to=file_upload.upload_to,verbose_name='ادرس عکس')


    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'تصاویر'





class MemeberCompany(models.Model):
    full_name = models.CharField(max_length=100,verbose_name='نام خانوادگی')
    file_upload = funcs.FileUpload('images','memeber_company')
    image_name = models.ImageField(upload_to=file_upload.upload_to,verbose_name='ادرس عکس')
    cerfigicated = models.CharField(max_length=100,verbose_name='عضو شرکت')
    is_active = models.BooleanField(default=True)
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')


    def __str__(self) -> str:
        return self.full_name



    class Meta:
        verbose_name = 'عضو شرکت'
        verbose_name_plural = 'اعضای شرکت'