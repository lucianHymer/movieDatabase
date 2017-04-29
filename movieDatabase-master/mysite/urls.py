"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import *
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^register/$', register),
	url(r'^$', home_page),
	url(r'^login/$', log_in),
	url(r'^logout/$', log_out),
	url(r'^promote/$', promote),
	url(r'^edit_movie/update_id=(\d+)$', edit_movie),
	url(r'^edit_movie/$', edit_movie),
	url(r'^modify_movie/$', modify_movie),
	url(r'^modify_crew/$', modify_crew),
	url(r'^edit_crew/update_id=(\d+)$', edit_crew),
	url(r'^edit_crew/$', edit_crew),
	url(r'^search/$', search),
	url(r'^add_tag/$', add_tag),
    url(r'^movie/$', movie),
    url(r'^manager_page/$', manager_page),
    url(r'^add_review/$', add_review)

]
