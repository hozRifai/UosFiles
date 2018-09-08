from django.urls import path , include , re_path

from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView,
)

app_name = 'users'
urlpatterns = [
    path('login/' , LoginView.as_view() , name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('dashboard/' , views.redirectToDashboard  , name="dashboard"),
    path("signup/" , views.signup, name='signup'),
    path('password_change/', PasswordChangeView.as_view( success_url='users/password_change/done/'), name="password_change"),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password_reset/', PasswordResetView.as_view(success_url='done/'), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view( success_url='/users/reset/done/'), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    re_path(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^user/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='user'),
]