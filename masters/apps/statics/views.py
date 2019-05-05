from django.shortcuts import render
from masters.apps.courses.models import Course

# Create your views here.
def home_view(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'statics/home.html', context)
