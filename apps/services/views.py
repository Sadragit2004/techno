from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from .models import Service,Service_Gallery,GroupService,Meta_tag_model
from apps.company.models import Company_Information
# Create your views here.


class ShowServiceView(View):

    def get(self, request, *args, **kwargs):
        # Fetch company information
        company_information = Company_Information.objects.filter(id=2).first()

        # Fetch active services
        service_app = Service.objects.filter(is_active=True).order_by('-register_date')

        # Paginate services
        paginator = Paginator(service_app, 5)  # Show 5 services per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'company': company_information,
            'services': page_obj  # Use `page_obj` for paginated services
        }

        return render(request, 'service_app/service.html', context)



class DetailService(View):

    def get(self, request, *args, **kwargs):
        # دریافت slug از URL
        slug = kwargs['slug']

        # دریافت اطلاعات شرکت
        company_information = Company_Information.objects.filter(id=2).first()

        # دریافت سرویس مورد نظر
        service = get_object_or_404(Service, slug=slug)

        # دریافت اطلاعات متا مرتبط با سرویس (اگر وجود داشته باشد)
        meta_tag = Meta_tag_model.objects.filter(service=service).first()

        # گروه‌های فعال
        groups = GroupService.objects.filter(is_active=True)

        # ساخت context
        context = {
            'company': company_information,
            'service': service,
            'groups': groups,
            'meta_tag': meta_tag,  # افزودن متا تگ به context
        }




        return render(request,'service_app/serviceDetail.html',context)





def ShowMainService(request):

     services = Service.objects.filter(is_active = True).order_by('-register_date')[:6]
     return render(request,'service_app/service_main.html',{'services':services})



def NewShowMainService(request):

     services = Service.objects.filter(is_active = True).order_by('-register_date')[:6]
     return render(request,'service_app/newmainservice.html',{'services':services})

