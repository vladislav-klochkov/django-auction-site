"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.generic.base import TemplateView, RedirectView

from AuctionApp.views import *
from django.conf.urls import url, include

from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^register/', register),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/browse'}, name='logout'),
    url(r'^profile/', view_profile),

    url(r'^create/', CreateAuction.as_view()),
    url(r'^saveauction/', save_auction),
    url(r'^browse/(?P<id>[0-9]+)/', browse_auction),
    url(r'^browse/', browse, name='browse'),
    url(r'^edit/(?P<id>[0-9]+)/', EditAuction.as_view()),
    url(r'^bid/(?P<id>[0-9]+)/', BidAuction.as_view()),
    url(r'^ban/(?P<id>[0-9]+)/', ban_auction),

    url(r'^language/', change_language),
    url(r'^currency/', change_currency),

    # enable the django's language redirect view
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'$^', RedirectView.as_view(url='browse/'), name='browse'),
]
