from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
import funcs
# Create your models here.

class Main_Slider(models.Model):
    title = models.CharField(max_length=40,verbose_name='عنوان')
    description2 = RichTextUploadingField(verbose_name='2توضیحات',config_name = 'special',blank = True)
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')

    def __str__(self) -> str:
        return f'{self.title}'


    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'


class GalleryMain(models.Model):

    slider = models.ForeignKey(Main_Slider,on_delete=models.CASCADE,verbose_name='اسلایدر',related_name='main_img')
    image_file = funcs.FileUpload('images','slide_img')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='عکس اصلی',default='')
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')
    alt = models.CharField(max_length=100,verbose_name='متن جایگزین ',blank=True,null=True)

