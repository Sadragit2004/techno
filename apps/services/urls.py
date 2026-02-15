from django.urls import path
from .views import *

app_name = 'service'

urlpatterns = [

    path('services/',ShowServiceView.as_view(),name='services'),
    path('services/<str:slug>/',DetailService.as_view(),name='detail_service'),
    path('main_service/',ShowMainService,name='main_service'),
    path('NewShowService/',NewShowMainService,name='newservice')

]
