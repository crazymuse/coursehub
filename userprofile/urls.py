from django.conf.urls import url


from . import views

app_name='userprofile'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/detail/$',views.DetailView.as_view(),name='detail'),
]
