"""DRFdemo URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter, SimpleRouter

from DRFdemo import settings
from stuapp import views, views1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stuapp.urls')),
    #path('actors1/', views1.ActorListView.as_view())
    path('docs/', include_docs_urls(title='我的接口文档')),
]


#router = DefaultRouter()
router = SimpleRouter()

router.register('actors', views.ActorListView2, basename='actors')
router.register('movies', views.MovieListView, basename='movies')
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)