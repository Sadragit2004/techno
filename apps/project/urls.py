from django.urls import path
from .views import *

app_name = 'proj'

urlpatterns = [

    path('price_projects/',ProjectView.as_view(),name='projs'),
    path('projectDetail/<str:slug>/',ProjectDetailView.as_view(),name='projectDetail'),
    path('project_main/',ProjectViewMain.as_view(),name='projct_main'),
    path('member/',Member_of_company,name='member')

]
