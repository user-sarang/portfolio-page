from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.portfolio_list, name='portfolio_list'),
    url(r'^create/$', views.portfolio_create, name= 'portfolio_create'),
    url(r'^(?P<pk>\d+)/$', views.portfolio_detail, name= 'portfolio_detail'),
    url(r'^(?P<pk>\d+)/edit$', views.portfolio_edit, name= 'portfolio_edit'),
    url(r'^your-content/$', views.portfolio_your_content, name='portfolio_your_content')

]
