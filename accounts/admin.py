from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)
""" from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, ContactNumber, DeliveryAddress, PaymentOption

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('name', 'email')


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email', 'name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2'),
        }),
    )


class ContactNumberAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'number')
    list_filter = ('title',)
    search_fields = ('user__email', 'title', 'number')


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'address')
    list_filter = ('title',)
    search_fields = ('user__email', 'title', 'address')


class PaymentOptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number')
    search_fields = ('user__email', 'card_number')


admin.site.register(User, CustomUserAdmin)
admin.site.register(ContactNumber, ContactNumberAdmin)
admin.site.register(DeliveryAddress, DeliveryAddressAdmin)
admin.site.register(PaymentOption, PaymentOptionAdmin) """