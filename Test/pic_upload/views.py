from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Picture

# Create your views here.
class PicList(ListView):
    queryset = Picture.objects.all().order_by('-date')
    # ListView默认context_object_name是object_list
    # 给模板传去一个上下文，
    # 类似 reder(request,'xx.html', {"latest_picture_list":latest_picture_list})
    
    context_object_name = 'latest_picture_list'
    # 默认template_name = 'Appname/picture_list.html'
    # template_name = 'picture_list.html'

class PicDetail(DetailView):
    model = Picture
    # DetailView默认Context_object_name是picture
    # 下面是DetailView默认模板，可以换成自己的
    # template_name = 'pic_upload/picture_detail.html'
    # template_name = 'picture_detail.html'
class PicUpload(CreateView):
    model = Picture
    # 可以通过fields选项自定义需要显示的表单
    fields = ['title', 'image']
    # CreateView默认Context_object_name是form。
     # 下面是CreateView默认模板，可以换成自己模板
     # template_name = 'pic_upload/picture_form.html'
    # template_name = 'picture_form.html'