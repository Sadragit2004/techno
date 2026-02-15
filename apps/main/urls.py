from django.urls import path
from .views import main,Resum_company,show_main_slider,MainVideo

app_name = 'main'

urlpatterns = [

    path('',main,name='index'),
    path('resum_company/',Resum_company,name='resum'),
    path('show_main/',show_main_slider,name='show_slider'),
    path('video_klaymer/',MainVideo,name='video')

]
