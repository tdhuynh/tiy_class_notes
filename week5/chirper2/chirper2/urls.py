from django.conf.urls import url, include
from django.contrib import admin
from app.views import index_view, about_view, ChirpView, ChirpDetailView, ChirpCreateView, \
                      ChirpUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', index_view, name='index_view'),
    url(r'^chirps/$', ChirpView.as_view(), name='chirp_view'),
    url(r'^chirps/create/$', ChirpCreateView.as_view(), name='chirp_create_view'),
    url(r'^chirps/(?P<pk>\d+)/$', ChirpDetailView.as_view(), name="chirp_detail_view"),
    url(r'^chirps/(?P<pk>\d+)/update/$', ChirpUpdateView.as_view(), name="chirp_update_view"),
    url(r'^about/$', about_view, name='about_view'),
]
