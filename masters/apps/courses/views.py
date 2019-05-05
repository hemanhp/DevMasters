from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course


# Create your views here.


class CourseListView(ListView):
    template_name = "courses/course_list.html"
    model = Course


class CourseDetailView(DetailView):
    template_name = "courses/course_detail.html"
    model = Course
