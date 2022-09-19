from django.contrib import admin
from blog.models import Post
from blog.apps import BlogAdminConfig
from django.contrib.auth.models import User, Group

# Register your models here.
class BlogAdminArea(admin.AdminSite):
    site_header: str = 'Blog Admin Area'
    
blog_site = BlogAdminArea(name = 'BlogAdmin')

admin.site.register(Post)
blog_site.register(Post)
blog_site.register(User)
blog_site.register(Group)