from django.contrib import admin

# Register your models here.
class BookStoreAdminArea(admin.AdminSite):
    site_header: str = 'Bookstore Admin Area'
    
bookstore_site = BookStoreAdminArea(name = 'BookStoreAdmin')
