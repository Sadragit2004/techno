from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
import funcs

# Create your models here.


class GroupService(models.Model):
    title_group = models.CharField(max_length=100,verbose_name='عنوان گروه')
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')
    update_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ اپدیت')


    def __str__(self) -> str:
        return f'{self.title_group}'



    class Meta:
        verbose_name = 'گروه سرویس'
        verbose_name_plural = 'گروه های سرویس'





class Service(models.Model):

    title = models.CharField(max_length=150,verbose_name='عنوان خدمات',)
    summery = models.TextField(verbose_name='توضیح کوتاه')
    decription = RichTextUploadingField(verbose_name='2توضیحات',config_name = 'special',blank = True,null=True)
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')
    update_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ اپدیت')
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    image_file = funcs.FileUpload('img','service_img')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='ادرس عکس')
    group_service = models.ForeignKey(GroupService,on_delete=models.CASCADE,verbose_name='گروه سرویس ها',related_name='group_service')
    slug = models.CharField(max_length=50,verbose_name='اسلاگ',null=True,blank=True)
    decription_meta = models.TextField(verbose_name='توضیجان متا',null=True,blank=True)
    city_link = models.TextField(verbose_name='لینک شهر',blank=True,null=True)


    def __str__(self) -> str:
        return f'{self.title}'


    class Meta:
        verbose_name = 'سرویس'
        verbose_name_plural = 'سرویس ها'


class Meta_tag_model(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='service_meta', null=True, blank=True
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




class Service_Gallery(models.Model):

    image_file = funcs.FileUpload('img','service_img')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='ادرس عکس')
    Serviceice = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='گروه سرویس ها',related_name='img_service')
    is_active = models.BooleanField(default=True,verbose_name='فعال')