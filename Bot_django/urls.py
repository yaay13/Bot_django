from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bot/', include('bot.urls')),
    url(r'^user/', include('user.urls')),

]
