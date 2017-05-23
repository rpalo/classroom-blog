
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^classrooms/(?P<pk>[0-9]+)/$', views.ClassroomHomepage.as_view(), name='classroom-detail'),
    url(r'^blogs/(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile-detail'),
]