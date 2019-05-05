from django.contrib import admin
from .models import Course, CourseSection, CourseSectionItem
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


# Register your models here.
class CourseSectionItemInlineAdmin(NestedStackedInline):
    model = CourseSectionItem
    extra = 1

class CourseSectionInlineAdmin(NestedStackedInline):
    model = CourseSection
    extra = 1
    inlines = (CourseSectionItemInlineAdmin,)





@admin.register(Course)
class CourseAdmin(NestedModelAdmin):
    inlines = (CourseSectionInlineAdmin,)
