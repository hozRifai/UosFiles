from django.urls import path, include
from files.views import *
from django.views.generic import TemplateView
app_name = 'files'
urlpatterns = [
    path('documents/', model_form_upload, name='documents'),
    path('dashboard/', showDocuments, name="dashboard"),
    path('contact-us/' , contact , name="contact" ),
]
