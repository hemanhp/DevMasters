from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserProfile, User


# Register your models here.
class UserProfileAdminInline(admin.StackedInline):
    model = UserProfile


@admin.register(User)
class DevUserAdmin(UserAdmin):
    readonly_fields = ('last_login', 'date_joined')
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    inlines = (UserProfileAdminInline,)

