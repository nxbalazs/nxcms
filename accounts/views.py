from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from homepage.models import HomepageBody, PageSettings
from blog.models import BlogPost, BlogTags
from links.models import Links


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
        try:
            links_list = Links.objects.all()
        except:
            links_list = False
        context = {
            'admin': True,
            'homepage_body': homepage_body,
            'page_settings': page_settings,
            'links_list': links_list,
            'page_title': 'Dashboard',
        }
    else:
        context = {
            'admin': False,
            'page_title': 'Dashboard',
        }

    # edit homepage
    if 'homepage_form' in request.POST:
        title = request.POST.get('title')
        body = request.POST.get('body')
        body_post = HomepageBody(
            title=title,
            body=body
        )
        body_post.save()
        return redirect('homepage:homepage')

    # edit settings
    if 'site_settings_form' in request.POST:
        page_name = request.POST.get('page_name')
        footer_text = request.POST.get('footer_text')
        homepage_text = request.POST.get('homepage_text')
        blog_text = request.POST.get('blog_text')
        link_text = request.POST.get('link_text')
        login_text = request.POST.get('login_text')
        logout_text = request.POST.get('logout_text')
        dashboard_text = request.POST.get('dashboard_text')
        page_settings_post = PageSettings(
            name=page_name,
            footer_text=footer_text,
            menu1_text=homepage_text,
            menu2_text=blog_text,
            menu3_text=link_text,
            menu4_text=login_text,
            menu5_text=logout_text,
            menu6_text=dashboard_text,
        )
        page_settings_post.save()
        return redirect('homepage:homepage')

    # new blogpost
    if 'blogpost_form' in request.POST:
        title = request.POST.get('blog_title')
        body = request.POST.get('blog_body')
        tags = request.POST.get('blog_tags')
        separated_tags = tags.split(',')
        new_tags = []
        for tag in separated_tags:
            new_tag, _ = BlogTags.objects.get_or_create(tag=tag.lstrip())
            new_tags.append(new_tag)
        blog_post = BlogPost(
            title=title,
            body=body,
        )
        blog_post.save()
        blog_post.tags.add(*new_tags)
        return redirect('blog:blog')

    # add new link
    if 'link_form' in request.POST:
        link_name = request.POST.get('link_name')
        link_url = request.POST.get('link_url')
        link_url = link_url.replace('https://', '')
        link_url = link_url.replace('http://', '')
        link_url = link_url.replace('www.', '')
        new_link_post = Links(
            name=link_name,
            url=link_url,
        )
        new_link_post.save()
        return redirect('links:links')

    # remove link
    if 'rm_link_form' in request.POST:
        link_pk = request.POST.get('link_pk')
        Links.objects.filter(pk=link_pk).delete()
        return redirect('accounts:accounts')

    return render(request, 'accounts/dashboard.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:accounts')
    return render(request, 'accounts/login.html', {'page_title': 'Login', })


@login_required()
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage:homepage')
    return render(request, 'accounts/logout.html', {'page_title': 'Logout', })
