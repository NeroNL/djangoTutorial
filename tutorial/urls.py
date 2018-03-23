"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import *
from django.contrib import admin
from tutorial.contact import contact
from tutorial.view import hello, currentTime, hours_ahead, meta_data
from tutorial.testDb import testdb1, testdb2
from tutorial import search

admin.autodiscover()
urlpatterns = [url('^hello/$', hello),
               url('^testdb1/$', testdb1),
               url('^testdb2/$', testdb2),
               url('^search_form/$', search.search_form),
               url('^search/$', search.search),
               url('^post_form/$', search.search_post),
               url(r'admin/', include(admin.site.urls)),
               url(r'^currentTime$', currentTime),
               url(r'^currentTime/plus/\d+/$', hours_ahead),
               url(r'^metadata/$', meta_data),
               url(r'^contact/$', contact),
               url(r'^$', hello)
               ]
