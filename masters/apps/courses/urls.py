from django.urls import path
from .views import CourseListView,CourseDetailView, LessonView
urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<str:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('<str:course>/items/<str:item>', LessonView.as_view(), name="lesson")
]
