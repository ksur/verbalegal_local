"""verbalegal URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView

from website import views


urlpatterns = [
    url(r'^blog/$', RedirectView.as_view(url='http://verbalegal.pl/blog/index.php'), name='blog'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^oferta/$', views.oferta, name='oferta'),
    url(r'^onas/$', views.onas, name='onas'),
    url(r'^zamowienie/$', views.zamowienie, name='zamowienie'),
    url(r'^wyslij/$', views.wyslij, name='wyslij'),
]
