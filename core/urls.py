from core.views.index import IndexTemplateView
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [


    path('', IndexTemplateView.as_view(), name="index"),
   #  path('pt1/', views.pt1_new, name='pt1'),



 ]