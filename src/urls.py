from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^',include('course.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^course/',include('course.urls'))
]
