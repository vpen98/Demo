from django.urls import re_path
from . import views
app_name = 'request_demo'
urlpatterns = [
    re_path(r'^$',views.requestdemo, name='requestdemo'),
    # 如果是re_path(r'',views.requestdemo, name='requestdemo')
    # 那么不管怎么链接，下面的链接的网页始终显示的是上面的网页
    re_path(r'^testfind/$',views.Testfinddemo, name='testfinddemo')
]