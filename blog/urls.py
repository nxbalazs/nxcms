from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('<tag>/', views.blog_tag_view, name='blog_tag'),
    path('<int:pk>', views.blog_single_view, name='blog_single'),
]