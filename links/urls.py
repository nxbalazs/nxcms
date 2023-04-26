from django.urls import path
from . import views

app_name = 'links'

urlpatterns = [
    path('', views.links_view, name='links'),
]