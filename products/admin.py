from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage, Brand, Category, BrandCategory, ProductReview, FlagOption

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    list_filter = ('brand', 'category', 'flag')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="30" height="30"/>', obj.image.url)
        else:
            return '-'
    image_preview.short_description = 'Image'
    list_display = ['name', 'sku', 'price', 'quantity', 'image_preview', 'flag']
    
class BrandCategoryInline(admin.TabularInline):
    model = BrandCategory

class BrandAdmin(admin.ModelAdmin):
    inlines = [BrandCategoryInline]
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="30" height="30"/>', obj.image.url)
        else:
            return '-'
    image_preview.short_description = 'Image'
    list_display = ['name', 'image_preview']
    
class CategoryAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="30" height="30"/>', obj.image.url)
        else:
            return '-'
    image_preview.short_description = 'Image'
    list_display = ['name', 'image_preview']
    
class BrandCategoryAdmin(admin.ModelAdmin):
    list_filter = ('brand', 'category')
    
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rate', 'created_at')
    
class FlagOptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BrandCategory, BrandCategoryAdmin)
admin.site.register(FlagOption, FlagOptionAdmin)