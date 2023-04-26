from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from homepage.models import HomepageBody, PageSettings

# Create your views here.
@login_required()
def accounts_view(request):
    # check logged in user admin status
    if request.user.is_staff:
        # get homepage post for preview
        try:
            homepage_body = HomepageBody.objects.get(pk=1)
        except:
            homepage_body = False
        try:
            page_settings = PageSettings.objects.get(pk=1)
        except:
            page_settings = False
        context = {
            'admin': True,
            'homepage_body': homepage_body,
            'page_settings': page_settings,
        }
    else:
        context = {
            'admin': False,
        }

    # edit homepage
    if 'homepage_form' in request.POST:
        title = request.POST.get('title')
        body = request.POST.get('body')
        body_post = HomepageBody(
            title = title,
            body = body
        )
        body_post.save()
        return redirect('homepage:homepage')
    
    # edit settings
    if 'site_settings_form' in request.POST:
        page_name = request.POST.get('page_name')
        footer_text = request.POST.get('footer_text')
        page_settings_post = PageSettings(
            name = page_name,
            footer_text = footer_text
        )
        page_settings_post.save()
        return redirect('homepage:homepage')
    
    return render(request, 'accounts/dashboard.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:accounts')
    return render(request, 'accounts/login.html', {})


@login_required()
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage:homepage')
    return render(request, 'accounts/logout.html', {})