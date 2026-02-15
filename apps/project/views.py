from django.shortcuts import render,get_object_or_404
from apps.company.models import Company_Information
from django.core.paginator import Paginator
from django.views import View
from .models import Project,MemeberCompany,Meta_tag_model

# Create your views here.

class ProjectView(View):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(is_active=True).order_by('-register_date')
        company_information = Company_Information.objects.filter(id=2).first()

        # Pagination
        paginator = Paginator(projects, 10)  # Show 10 projects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'company': company_information,
            'projects':projects
        }
        return render(request, 'project_app/projects.html', context)




class ProjectDetailView(View):

    def get(self,request,*args, **kwargs):

        slug = kwargs['slug']
        project = get_object_or_404(Project,slug = slug)
        meta_tag = Meta_tag_model.objects.filter(projedct=project).first()
        company_information = Company_Information.objects.filter(id=2).first()
        return render(request,'project_app/projectDetail.html',{'project':project,'company':company_information,'meta_tag':meta_tag})





class ProjectViewMain(View):

    def get(self,request,*args, **kwargs):
        company_information = Company_Information.objects.filter(id=2).first()
        project = Project.objects.filter(is_active = True).order_by('-register_date')
        return render(request,'project_app/project_main.html',{'projects':project,'company':company_information})



def Member_of_company(request):

    members = MemeberCompany.objects.filter(is_active = True).order_by('register_date')
    return render(request,'project_app/member.html',{'members':members})