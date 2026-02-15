from django.shortcuts import render
from django.views import View
from .models import About_us,ManyQuestion
from apps.company.models import Company_Information

# Create your views here.


class About_usView(View):

    def get(self,request,*args, **kwargs):

        about = About_us.objects.filter(id = 1).first()
        company_information = Company_Information.objects.filter(id = 2).first()

        return render(request,'about_app/about.html',{'about':about,'company':company_information})


def ShowAboutMain(request):

    about = About_us.objects.filter(id = 1).first()
    company_information = Company_Information.objects.filter(id = 2).first()
    return render(request,'about_app/main_about.html',{'about':about,'company':company_information})




def MainManyQuestion(request):

    qus = ManyQuestion.objects.filter(is_active = True).order_by('-register_date')

    return render(request,'about_app/qus.html',{'quss':qus})