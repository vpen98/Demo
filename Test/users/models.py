from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def user_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join(instance.user.id, 'avatar', filename) # instance.user.id,

class UserProfile(models.Model):
    # 用户信息于用户一对一关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    org = models.CharField('住址', max_length=128, blank=True)
    telephone = models.CharField('电话号码', max_length=50, blank=True)
    mod_date = models.DateTimeField("最新一次更改", auto_now=True)
    nicename = models.CharField('昵称', max_length=32, blank=True, default="莫得感情的杀手")
    student_id = models.CharField('学号',max_length=32, blank=True)
    school = models.CharField('学校', max_length=128, blank=True)
    #picture = models.ImageField('头像',upload_to=user_dir_path,null=True,blank=True)
    
    class Meta:
        # 数据库表的名字
        db_table = "UserProfile"
        # 后台表的名称
        verbose_name = 'User Profile'
    
    def __str__(self):
        return "{}".format(self.user.__str__())