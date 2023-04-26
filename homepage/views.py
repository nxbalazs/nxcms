from django.shortcuts import render
from homepage.models import HomepageBody

# Create your views here.
def homepage(request):
    try:
        homepage_body = HomepageBody.objects.get(pk=1)
        context = {
            'homepage_body': homepage_body,
        }
    except:
        context = {
            'homepage_body': 'False',
        }

    return render(request, 'homepage/homepage.html', context)
