from django.db import models
from django.urls import reverse
import jdatetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


import funcs
# Create your models here.



# group page
class Group_blog(models.Model):
    group_name = models.CharField(max_length=100,verbose_name='گروه ')
    is_active = models.BooleanField(max_length=False,verbose_name='وضعیت')


    def __str__(self) -> str:
        return self.group_name





    class Meta:
        verbose_name = ' گروه مقاله'
        verbose_name_plural = 'گروه های مقاله'



# author
class Author(models.Model):
    Author_name = models.CharField(max_length=30,verbose_name='نویسنده')
    is_active = models.BooleanField(default=True,verbose_name='وضعیت')

    def __str__(self) -> str:
        return self.Author_name





    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = '  نویسنده ها'


# blog
class Blog(models.Model):
    name_blog = models.CharField(verbose_name='نام گروه',max_length=100,)
    subject = models.CharField(verbose_name='موضوع',max_length=300)
    grop_blog = models.ForeignKey(Group_blog,verbose_name='گروه مقاله',on_delete=models.CASCADE,related_name='group_of_blog')
    Auther_blog = models.ManyToManyField(Author,verbose_name='نویسنده مقاله')
    image_file = funcs.FileUpload('images','blog_image')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='عکس اصلی',default='')
    view = models.IntegerField(verbose_name='ویو')
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    time_read = models.CharField(max_length=30,verbose_name='تایم مطالعه')
    register_data = models.DateTimeField(verbose_name='تاریخ',auto_now_add=True)
    update_data = models.DateTimeField(verbose_name='اپدیت شده',auto_now_add=True)
    description = models.TextField(verbose_name='1توضیحات',blank = True)
    description2 = RichTextUploadingField(verbose_name='2توضیحات',config_name = 'special',blank = True)
    key_words = models.CharField(max_length=1000,verbose_name='کلمات کلیدی',null=True,blank=True)
    slug = models.CharField(verbose_name='اسلاگ',max_length=40)
    city_link = models.TextField(verbose_name='لینک شهر',blank=True,null=True)






    def __str__(self):
        return f'{self.subject}'

    def time_since_posted(self):
        now = timezone.now()
        diff = now - self.register_data

        if diff.days == 0 and diff.seconds < 60:
            return 'چند لحظه پیش'
        if diff.days == 0 and diff.seconds < 3600:
            minutes = diff.seconds // 60
            return f'{minutes} دقیقه پیش'
        if diff.days == 0 and diff.seconds < 86400:
            hours = diff.seconds // 3600
            return f'{hours} ساعت پیش'
        if diff.days < 30:
            return f'{diff.days} روز پیش'
        if diff.days < 365:
            months = diff.days // 30
            return f'{months} ماه پیش'
        years = diff.days // 365
        return f'{years} سال پیش'


    # make a jalalitime
    def get_jalali_register_date(self):
        return jdatetime.datetime.fromgregorian(datetime=self.register_data).strftime('%Y/%m/%d')


    # func for go to ther detail

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug })




    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'




class Meta_tag_model(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='blog_meta', null=True, blank=True
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










class Lable_blog(models.Model):

    title = models.CharField(max_length=30,verbose_name='برچسب')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name='مقالات',related_name='blog_lable',null=True,blank=True)






class Comment(models.Model):
    full_name = models.CharField(max_length=100,verbose_name='اسم کامل',)
    email = models.CharField(verbose_name='ایمیل',max_length=100,null=True,blank=True)
    text = models.TextField(verbose_name='پیام')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name='مقالات',related_name='comment_blog')
    is_active = models.BooleanField(default=False)
    register_data = models.DateTimeField(verbose_name='تاریخ',default=timezone.now())

    def __str__(self) -> str:
        return f'{self.full_name}'


    def get_jalali_register_date(self):
        return jdatetime.datetime.fromgregorian(datetime=self.register_data).strftime('%Y/%m/%d')


