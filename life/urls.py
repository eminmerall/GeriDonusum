"""life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from earth.views import home_view
from earth.views import hakkimizda_view
from earth.views import iletisim_view
from earth.views import geridonusum_view
from earth.views import kayiol_view
from earth.views import randevu_view
from earth.views import randevuu_view
from earth.views import index_view
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from earth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('hakkimizda/', hakkimizda_view),
    path('iletisim/', iletisim_view),
    path('geridonusum/', geridonusum_view),
    path('kayitol/', kayiol_view),
    path('randevu/', randevu_view),
    path('randevuu/', randevuu_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', index_view),


    url(r'^admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)