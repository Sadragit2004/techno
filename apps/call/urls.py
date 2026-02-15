from django.urls import path
from .views import *

app_name = 'call'

urlpatterns = [

    path('call/',CallView.as_view(),name='call')

]
