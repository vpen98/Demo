from django.urls import re_path
from . import views

app_name = "user"
urlpatterns = [
    re_path(r'^register/$', views.register, name="register"),
    re_path(r'^$',views.login, name='login'),
    re_path(r'^user/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    re_path(r'^user/(?P<pk>\d+)/profile/update/$',views.profile_update, name="profile_update"),
    re_path(r'^user/(?P<pk>\d+)/pwdchange/$', views.pwd_change, name='pwd_change'),

]