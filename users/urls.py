from django.urls import path , include
from . import views
from django.views.generic import TemplateView

app_name = 'users'
urlpatterns = [
    path('' , include('django.contrib.auth.urls')),
    path('dashboard/' , views.redirectToDashboard  , name="dashboard"),
    path("signup/" , views.SignUp.as_view(), name='signup'),
]