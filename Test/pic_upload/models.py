from django.db import models
from datetime import date
from django.urls import reverse
from django.utils.html import format_html
import uuid
import os

# Create your models here.
def user_dir_path(instance, imagename):
    ext = imagename.split('.')[-1] # 获取文件后缀名
    imagename = '{}.{}'.format(uuid.uuid4().hex[:10], ext) # uuid.uuid4().hex[:10]生成随机名
    return os.path.join('picture', imagename)

class Picture(models.Model):
    title = models.CharField('标题', max_length=100,blank=True, default='unname')
    image = models.ImageField('图片', upload_to=user_dir_path, blank=True)
    date = models.DateField(verbose_name='上传时间', default=date.today)

    def image_data(self):
        image_html = '<img src="{}" width="100px"/>'
        return format_html(image_html,self.image.url)
    # short_description 设置标题 相当于设置verbose_name
    image_data.short_description = u'图片'
    
    class Meta:
        db_table = 'picture' # 数据库表名
        
    def __str__(self):
        return self.title
    
    '''
    # 对于使用Django自带的通用视图非常重要
    Django自带通用视图在完成对象编辑或创建后需要一个返回页面，
    所以我们必需在模型里定义一个返回链接get_absolute_url。
    在本项目中，图片上传成功后，用户会跳转到图片详情页面
    '''
    def get_absolute_url(self):
        return reverse('pic_upload:pic_detail', args=[str(self.id)])