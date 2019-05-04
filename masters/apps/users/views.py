from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import View


class DevLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class DevLogoutView(LogoutView):
    template_name = 'users/logout.html'


class ProfileDashboardView(View):
    def get(self, request):
        return render(request, 'users/profile_dashboard.html')


class ProfileCourses(View):
    def get(self, request):
        return render(request, 'users/profile_courses.html')
