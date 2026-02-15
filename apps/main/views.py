from django.shortcuts import render
import kelaymer.settings as sett
from apps.company.models import Company_Information
from .models import Main_Slider
# Create your views here.


def media_admin(request):
    context = {
        'media_url':sett.MEDIA_URL
    }


    return context


def main(request):

    company_information = Company_Information.objects.filter(id = 2).first()

    context = {

        'company':company_information,

    }

    return render(request,'main_app/main.html',context)






def Resum_company(request):

    company_information = Company_Information.objects.filter(id = 2).first()

    context = {
        'company':company_information,
    }

    return render(request,'main_app/resum_company.html',context)



def show_main_slider(request):

    sliders = Main_Slider.objects.filter(id = 10).first()
    company_information = Company_Information.objects.filter(id = 2).first()
    return render(request,'main_app/main_slider.html',{'sliders':sliders,'company':company_information})



def MainVideo(request):

    company_information = Company_Information.objects.filter(id = 2).first()

    return render(request,'blog_app/video.html',{'video':company_information})