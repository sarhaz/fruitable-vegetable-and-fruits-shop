from django.contrib import admin
from home.models import Category, Product, Profile, Client
from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_display_links = ('id', 'name', 'price', 'category')


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_display_links = ('id', 'first_name', 'last_name', 'email')


@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'profession', 'rating')
    list_display_links = ('id', 'first_name', 'last_name', 'profession', 'rating')
