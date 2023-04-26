from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from homepage.models import HomepageBody

# Create your views here.
@login_required()
def accounts_view(request):
    # check logged in user admin status
    if request.user.is_staff:
        # get homepage post for preview
        homepage_body = HomepageBody.objects.get(pk=1)
        context = {
            'admin': 'True',
            'homepage_body': homepage_body,
        }
    else:
        context = {
            'admin': 'False',
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
    
    return render(request, 'accounts/dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:accounts')
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage:homepage')
    return render(request, 'accounts/logout.html', {})