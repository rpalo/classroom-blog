
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^classrooms/(?P<pk>[0-9]+)/$', views.ClassroomHomepage.as_view(), name='index'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
]