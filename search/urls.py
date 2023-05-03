from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'search'
router = DefaultRouter()
router.register('search', views.SearchViewSet)

urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
]