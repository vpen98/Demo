from django.db import models
from django.contrib.auth.models import User
import uuid
import os
# Create your models here.

# 给上传的文件命名，返回一个路径
def user_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join('avatar', filename) # instance.user.id,

class File(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "file")
    file = models.FileField(upload_to=user_dir_path, null= True)
    upload_method = models.CharField("上传文件类型", max_length=20)