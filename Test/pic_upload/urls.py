from django.urls import path, re_path
from . import views
# namespace
app_name = 'pic_upload'
urlpatterns = [
    # 展示所有图片
    re_path('^$',views.PicList.as_view(), name='pic_list'),
    # 上传图片
    re_path(r'^pic/upload/$', views.PicUpload.as_view(), name='pic_upload'),
    # 展示图片
    re_path(r'^pic/(?P<pk>\d+)/$', views.PicDetail.as_view(), name='pic_detail'),
]