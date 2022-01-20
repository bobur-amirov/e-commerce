from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode

from .models import UserBase
from .forms import UserBaseRegisterForm
from .token import account_activation_token


def dashboard(request):

    return render(request, 'account/dashboard.html')


def user_register(request):
    if request.method == 'POST':
        form = UserBaseRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            })
            user.email_user(subject=subject, message=message)


    else:
        form = UserBaseRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'account/registration/register.html', context)


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_encode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except():
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/account_invalid.html')