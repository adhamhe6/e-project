from django.contrib import admin
from django.utils.html import format_html
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']

admin.site.register(Company, CompanyAdmin)