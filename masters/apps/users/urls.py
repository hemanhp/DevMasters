from .views import DevLoginView, DevSignupView, DevLogoutView, ProfileCourses, ProfileDashboardView, EditProfile
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('login/', DevLoginView.as_view(), name='login'),
    path('register/', DevSignupView.as_view(), name='register'),
    path('logout/', DevLogoutView.as_view(), name='logout'),
    #
    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('profile/', ProfileDashboardView.as_view(), name="profile_dashboard"),
    path('profile/courses', ProfileCourses.as_view(), name="profile_courses"),
    path('profile/edit', EditProfile.as_view(), name="profile_edit")
]

