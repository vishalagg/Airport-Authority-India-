from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^apron1/$',views.AprononeListView.as_view(),name='apronone'),
    url(r'^apron2/$',views.AprontwoListView.as_view(),name='aprontwo'),
    url(r'^apron3/$',views.ApronthreeListView.as_view(),name='apronthree'),
    url(r'^emergency/$',views.EmergencyListView.as_view(),name='emergency'),
    url(r'^apron1/(?P<pk>\d+)$', views.AprononeDetailView.as_view(), name='apronone-detail'),
    url(r'^apron2/(?P<pk>\d+)$', views.AprontwoDetailView.as_view(), name='aprontwo-detail'),
    url(r'^apron3/(?P<pk>\d+)$', views.ApronthreeDetailView.as_view(), name='apronthree-detail'),
    url(r'^emergency/(?P<pk>\d+)$', views.EmergencyDetailView.as_view(), name='emergency-detail'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^about/$',views.about,name='about'),
    url(r'^tandc/$',views.tandc,name='tandc'),
    url(r'^privacy/$',views.privacy,name='privacy'),
]