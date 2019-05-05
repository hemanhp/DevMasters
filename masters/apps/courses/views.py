from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Course,CourseSectionItem


# Create your views here.


class CourseListView(ListView):
    template_name = "courses/course_list.html"
    model = Course


class CourseDetailView(DetailView):
    template_name = "courses/course_detail.html"
    model = Course


class LessonView(View):
    def get(self, request, course, item):
        context = {
            'course': get_object_or_404(Course, slug=course),
            'item': get_object_or_404(CourseSectionItem, slug=item)
        }
        return render(request, "courses/lesson.html", context)
