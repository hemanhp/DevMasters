from django.contrib import admin
from .models import Course


# Register your models here.

# @admin.register(Author)
# class AuthorsAdmin(admin.ModelAdmin):
#     list_display = ('full_name',)
#     prepopulated_fields = {"slug": ("full_name",)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
