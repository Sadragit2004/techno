from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import funcs
from django.utils import timezone
# Create your models here.


class About_us(models.Model):
    title = models.CharField(max_length=100,verbose_name='حروف')
    decription = RichTextUploadingField(verbose_name='2توضیحات',config_name = 'special',blank = True,null=True)
    image_file = funcs.FileUpload('img','company_img')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='ادرس عکس')
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')



    def __str__(self) -> str:
        return f'{self.title}'



    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'




class ManyQuestion(models.Model):

    question = models.CharField(max_length=300,verbose_name='سوال')
    answer = models.TextField(verbose_name='جواب')
    is_active = models.BooleanField(verbose_name='وضعیت',default=True)
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')
    video_file = funcs.FileUpload('video','feq')
    video = models.FileField(verbose_name='ودیو',upload_to=video_file.upload_to,null=True,blank=True)


    def __str__(self) -> str:
        return f'{self.question}'


    class Meta:

        verbose_name = 'سوالات متداول'
        verbose_name_plural = 'سوالات'