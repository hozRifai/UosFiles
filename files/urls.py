from django.urls import path, include
from files.views import *
from django.views.generic import TemplateView
app_name = 'files'
urlpatterns = [
    path('', TemplateView.as_view(template_name="files.html"), name="files"),
    path('documents/', model_form_upload, name='documents'),
    path('dashboard/', showDocuments, name="dashboard"),
    path('contact-us/' , contact , name="contact" ),
]
