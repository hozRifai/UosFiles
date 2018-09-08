from django.shortcuts import render , redirect , reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes , force_text
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your UosFiles Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('users:account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('files:dashboard'))
    else:
        return render(request, 'account_activation_invalid.html')

def redirectToDashboard(request):
    return HttpResponseRedirect(reverse('files:dashboard'))

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')