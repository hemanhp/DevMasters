from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Course, CourseCategory, CourseSectionItem, CourseEnrollment


# Create your views here.


class CourseListView(ListView):
    template_name = "courses/course_list.html"
    model = Course

    def get_queryset(self):
        if self.request.GET.get("category"):
            slug = self.request.GET["category"]
            return Course.objects.all().filter(published=True, categories__slug=slug)
        else:
            return Course.objects.all().filter(published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context["categories"] = CourseCategory.objects.all()
        return context


class CourseDetailView(DetailView):
    template_name = "courses/course_detail.html"
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated and CourseEnrollment.objects.all().filter(user_id=self.request.user.id,
                                                                                        course=kwargs.get(
                                                                                                'object')).exists():
            context["enrolled"] = True
        else:
            context["enrolled"] = False

        return context


class LessonView(View):
    def get(self, request, course, item):
        course = get_object_or_404(Course, slug=course)
        context = {
            'course': course,
            'item': get_object_or_404(CourseSectionItem, slug=item),
            'enrolled': CourseEnrollment.objects.filter(course_id=course.id, user_id=request.user.id).exists()
        }
        return render(request, "courses/lesson.html", context)


class CourseEnrollmentView(LoginRequiredMixin, View):
    def get(self, request, course):
        course = get_object_or_404(Course, slug=course)
        user = request.user
        enroll = CourseEnrollment(user_id=user.id, course_id=course.id)
        enroll.save()
        return redirect(reverse('lesson', kwargs={'course': course.slug,  'item': course.coursesection_set.all()[0].coursesectionitem_set.all()[0].slug}))
