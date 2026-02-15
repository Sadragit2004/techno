from django.shortcuts import render
from django.views import View
from apps.company.models import Company_Information
# Create your views here.

class CallView(View):

    def get(self,request,*args, **kwargs):
        company_information = Company_Information.objects.filter(id=2).first()

        context = {
            'company':company_information
        }

        return render(request,'call_app/call.html',context)