from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ChoiceDetailView.as_view(), name='detail'),
    url(r'^forms/$', views.create_choice, name='create_choice'),
    url(r'^update/(?P<pk>\d+)/$', views.update_choice, name='update'), 
    url(r'^delete/(?P<pk>\d+)/$', views.delete_choice, name='delete'),
    url(r'^some_view/$', views.some_view, name='some_view')
    ]

