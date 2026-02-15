from django.urls import path
from .views import *

app_name = 'about'

urlpatterns = [

    path('about-us/',About_usView.as_view(),name='about'),
    path('main_about/',ShowAboutMain,name='about_me'),
    path('show_question/',MainManyQuestion,name='qus')

]
