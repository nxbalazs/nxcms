from django.shortcuts import render
from blog.models import BlogPost, BlogTags

# Create your views here.
def blog_view(request):
    blog_post = BlogPost.objects.all().order_by('-created_date')
    context = {
        'blog_posts': blog_post,
    }
    return render(request, 'blog/blog.html', context)

def blog_tag_view(request, tag):
    blog_posts = BlogPost.objects.filter(tags__tag__contains=tag).order_by('-created_date')
    context = {
        "tag": tag,
        "blog_posts": blog_posts,
    }
    return render(request, 'blog/blog_tag.html', context)

def blog_single_view(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog/blog_single.html', {'blog_post': blog_post})
