"""masters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from masters.apps.statics.views import home_view
from django.conf.urls.static import static
from masters.apps.courses import sitemaps as course_sitemaps
from masters.apps.statics import  sitemaps as static_sitemaps

urlpatterns = [
    path('', home_view, name="home"),
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('masters.apps.users.urls')),
    path('courses/', include('masters.apps.courses.urls')),
    path('statics/', include('masters.apps.statics.urls'))
]

sitemaps = {
    'static': static_sitemaps.StaticSitemap,
    'courses': course_sitemaps.CourseSitemap,
    'lessons': course_sitemaps.CourseLessonSitemap
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += [
#         re_path(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), ServeProtectedMedia.as_view())
#     ]
