from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import get_user_model
from .forms import SignUpForm
from masters.apps.courses.models import CourseEnrollment
User = get_user_model()

class DevLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class DevSignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('profile_dashboard')
        return render(request, 'users/signup.html', {'form': form})


class DevLogoutView(LogoutView):
    template_name = 'users/logout.html'


class ProfileDashboardView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'users/profile_dashboard.html')


class ProfileCourses(LoginRequiredMixin,View):
    def get(self, request):
        context = {
            'courses': CourseEnrollment.objects.all().filter(user_id=request.user.id)
        }
        return render(request, 'users/profile_courses.html', context)


class EditProfile(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'users/profile_edit.html')

    def post(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.save()
        request.user = user
        return render(request, 'users/profile_edit.html')