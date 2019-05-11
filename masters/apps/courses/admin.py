from django.contrib import admin
from .models import Course, CourseKeyPoint, CourseSection, CourseSectionItem, CourseCategory, CourseEnrollment

# Register your models here.
class CourseSectionItemInlineAdmin(admin.StackedInline):
    model = CourseSectionItem
    prepopulated_fields = {'slug': ('title',), }
    extra = 1


class CourseSectionInlineAdmin(admin.StackedInline):
    model = CourseSection
    extra = 1


class CourseKeyPointInlineAdmin(admin.StackedInline):
    model = CourseKeyPoint
    extra = 3


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(CourseSection)
class CourseSectionAdmin(admin.ModelAdmin):
    inlines = (CourseSectionItemInlineAdmin,)
    list_display = ('course_title', 'title')

    def course_title(self, obj):
        return obj.course.title

    course_title.short_description = 'Course'
    course_title.admin_order_field = 'course__title'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    inlines = (CourseSectionInlineAdmin, CourseKeyPointInlineAdmin)


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enroll_date', 'enroll_type')
