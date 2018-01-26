from django.conf.urls import include, url
from django.contrib import admin
from Measure import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'WaxMeasure.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^wax_measure/hello$', views.hello),
    url(r'^wax_measure/tourist$', views.tourist),
    url(r'^wax_measure/upload$', views.upload),
    url(r'^wax_measure/download$', views.download),
]
