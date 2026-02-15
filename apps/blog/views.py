from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from apps.company.models import Company_Information
from .models import Blog,Comment,Meta_tag_model
from django.core.paginator import Paginator
from .forms import CommentForm
from django.contrib import messages

# Create your views here.


class ShowBlogView(View):
    def get(self, request, *args, **kwargs):
        blogs_list = Blog.objects.filter(is_active=True).order_by('-register_data')
        company_information = Company_Information.objects.filter(id=2).first()

        # Pagination setup
        page_number = request.GET.get('page', 1)  # Get current page number from the request
        paginator = Paginator(blogs_list, 5)  # Show 5 blogs per page
        blogs = paginator.get_page(page_number)  # Get the blogs for the current page


        context = {
            'blogs': blogs,
            'company': company_information,
        }

        return render(request, 'blog_app/blog.html', context)



class Blog_Detail(View):

    def get(self,request,*args, **kwargs):

        form = CommentForm()
        slug = kwargs['slug']
        
        blog = get_object_or_404(Blog,slug = slug)
        blog.view+=1
        blog.save()
        comments = Comment.objects.filter(is_active = True,blog = blog).order_by('-register_data')
        meta_tag = Meta_tag_model.objects.filter(blog=blog).first()
        company_information = Company_Information.objects.filter(id=2).first()
        blogs_list = Blog.objects.filter(is_active=True).order_by('register_data')[:1]
        context = {

            'blog':blog,
            'company': company_information,
            'blogs':blogs_list,
            'form':form,
            'comments':comments,
            'meta_tag':meta_tag
        }

        return render(request,'blog_app/blog_detail.html',context)



    def post(self,request,*args, **kwargs):

        slug = kwargs['slug']  # دریافت slug از URL
        blog = get_object_or_404(Blog, slug=slug)

        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment.objects.create(
                full_name = data['full_name'],
                email = data['email'],
                text = data['text'],
                blog = blog
            )

            messages.success(request,'نظر شما با موفقیت ارسال شد','success')
            return redirect('main:index')

        else:

            messages.error(request,'نظر شما با مشکل مواجه  شد','error')
            return redirect('main:index')




def Show_main_blog(request):

    blogs_list = Blog.objects.filter(is_active=True).order_by('-update_data')[:45]
    return render(request,'blog_app/main_blog.html',{'blogs':blogs_list})