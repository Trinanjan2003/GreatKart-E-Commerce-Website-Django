from django.contrib import admin

# Custom Imports
from .models import Category


# Register your models here : 

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name','slug')

admin.site.register(Category,CategoryAdmin)
