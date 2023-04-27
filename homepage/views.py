from django.shortcuts import render
from homepage.models import HomepageBody

# Create your views here.
def homepage(request):
    try:
        homepage_body = HomepageBody.objects.get(pk=1)
        context = {
            'homepage_body': homepage_body,
            'page_title': 'Homepage',
        }
    except:
        context = {
            'homepage_body': 'False',
            'page_title': 'Homepage',
        }

    return render(request, 'homepage/homepage.html', context)
