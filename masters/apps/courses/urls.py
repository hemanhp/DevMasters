from django.urls import path
from .views import CourseListView,CourseDetailView, LessonView, CourseEnrollmentView
urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<str:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('<str:course>/items/<str:item>/', LessonView.as_view(), name="lesson"),
    path('<str:course>/enroll/', CourseEnrollmentView.as_view(), name="enrollment")
]
