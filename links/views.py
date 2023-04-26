from django.shortcuts import render
from links.models import Links

# Create your views here.
def links_view(request):
    links = Links.objects.all()
    context = {
        'linkslist': links,
    }
    return render(request, 'links/links.html', context)