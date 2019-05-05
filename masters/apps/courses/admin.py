from django.contrib import admin
from .models import Course, CourseSection, CourseSectionItem, CourseCategory
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


# Register your models here.
class CourseSectionItemInlineAdmin(NestedStackedInline):
    model = CourseSectionItem
    prepopulated_fields = {'slug': ('title',), }
    extra = 1


class CourseSectionInlineAdmin(NestedStackedInline):
    model = CourseSection
    extra = 1
    inlines = (CourseSectionItemInlineAdmin,)


@admin.register(CourseCategory)
class CourseCategoryAdmin(NestedModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Course)
class CourseAdmin(NestedModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    inlines = (CourseSectionInlineAdmin,)
