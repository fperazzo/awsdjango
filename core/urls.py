from core.views.index import IndexTemplateView
from core.views.profile import update_profile

from django.urls import path


app_name = 'core'

urlpatterns = [


    path('', IndexTemplateView.as_view(), name="index"),
    
    path('profile', update_profile, name='updateprofile'),



 ]