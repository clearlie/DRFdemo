from django.urls import path, re_path
from rest_framework.documentation import include_docs_urls

from stuapp import views1, views3
from . import views


urlpatterns = [
    path('actors/', views.ActorListView.as_view()),
    path('actors/latest/', views3.ActorListView.as_view({'get': 'latest'})),
    path('actors1/', views1.ActorListView.as_view()),
    path('movies/', views1.MovieListView.as_view()),
    re_path(r'^actors/(?P<pk>\d+)/$', views.ActorDetilView.as_view()),
    re_path(r'^actors/(?P<pk>\d+)/$', views1.ActorListView1.as_view()),
    re_path(r'^actors/(?P<pk>\d+)/age/$', views3.ActorListView.as_view({'put': 'age'})),
    #path('docs/', include_docs_urls(title='我的接口文档')),
]