from django.contrib import admin
from blog.models import BlogPost, BlogTags
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, PostAdmin)
admin.site.register(BlogTags, TagAdmin)
