from django.urls import path
from .views import AboutUsView,ContactView,ComplaintView
urlpatterns = [
    path('about',AboutUsView.as_view(), name="about_us"),
    path('contact',ComplaintView.as_view(), name="contact_us"),
    path('complaint',ComplaintView.as_view(), name="complaint"),
]
