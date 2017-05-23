
from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.ClassroomHomepage.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
]