from django.shortcuts import render
from django.views import View

from masters.apps.courses.models import Course


# Create your views here.
def home_view(request):
    context = {
        'courses': Course.objects.all().filter(published=True)
    }
    return render(request, 'statics/home.html', context)


class AboutUsView(View):
    def get(self, request):
        return render(request, 'statics/aboutus.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'statics/contact.html')

class ComplaintView(View):
    def get(self, request):
        return render(request, 'statics/complaint.html')