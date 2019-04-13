from django.conf.urls import url
from . import views

app_name='course'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^login/$',views.login_user,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
	url(r'^register/$',views.UserFormView.as_view(),name='register'),

]
