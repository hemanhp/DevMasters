from django.urls import path
from .views import CourseListView,CourseDetailView
urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail')
]
