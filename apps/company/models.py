from django.db import models
import funcs
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Company_Information(models.Model):

    name_company = models.CharField(max_length=50,verbose_name='نام شرکت',)
    phone_number = models.CharField(verbose_name='تلفن شرکت',max_length=100)
    mobile_number = models.CharField(verbose_name='شماره موبایل',max_length=11)
    email = models.EmailField(verbose_name='یمیل')
    address = models.TextField(verbose_name='ادرس')
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')
    update_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ اپدیت')
    address_link = models.CharField(max_length=1000,verbose_name='ادرس لینک گوکل')
    image_file = funcs.FileUpload('img','logo')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='ادرس عکس')
    video_file = funcs.FileUpload('video','feq')
    video = models.FileField(verbose_name='ودیو',upload_to=video_file.upload_to,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.name_company}'


    class Meta:
        verbose_name = 'اطلاعات شرکت'
        verbose_name_plural = 'اطلاعات درباره شرکت'



class Resum_Company(models.Model):

    company = models.ForeignKey(Company_Information,on_delete=models.CASCADE,verbose_name='شرکت',related_name='resum_com')
    subject = models.CharField(max_length=100)
    decription = RichTextUploadingField(verbose_name='2توضیحات',config_name = 'special',blank = True,null=True)
    title_subject  = models.CharField(max_length=10,verbose_name='نتیجه')
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ')
    update_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ اپدیت')
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    image_file = funcs.FileUpload('img','company_img')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='ادرس عکس')
    letter = models.CharField(max_length=10,verbose_name='تک  کلمه ای',blank=None,null=True)


    def __str__(self):
        return f'{self.subject}'


    class Meta:
        verbose_name = 'رزومه شرکت'
        verbose_name_plural = 'رزومه های شرکت'



class Social_Media(models.Model):

    company = models.ForeignKey(Company_Information,on_delete=models.CASCADE,verbose_name='شرکت',related_name='social_company')
    name_social = models.CharField(max_length=20,verbose_name='نام شبکه اجتماعی')
    icon = models.TextField(verbose_name='ادرس ایکون شبکه اجتماعی',null=True,blank=True)
    image_file = funcs.FileUpload('img','logo')
    image_name = models.ImageField(upload_to=image_file.upload_to,verbose_name='ادرس عکس',null=True,blank=True)
    address_link = models.CharField(max_length=1000,verbose_name='ادرس لینک ')



    def __str__(self) -> str:
        return f'{self.name_social}'



    class Meta:

        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماهی'