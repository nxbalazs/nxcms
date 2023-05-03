# from django.shortcuts import render
from rest_framework import viewsets, filters
from blog.models import BlogPost
from .serializers import BlogSerializer
from django.http import JsonResponse
from django.views import View


# Create your views here.
class SearchViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'pk']


class SearchView(View):
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        if search:
            blog_posts = BlogPost.objects.filter(title__icontains=search).values('pk', 'title')
            results = list(blog_posts)
            return JsonResponse({'results': results})
        return JsonResponse({})
