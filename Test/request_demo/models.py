from django.db import models
from django.utils import timezone
# Create your models here.
class Book(models.Model):
    # choice接收一个二维数组，
    # 每一个选项是由一个元组（value,display_name）构成。
    # display_name就是要在页面中展示的。
    # 模板中{{Book.book_type}}显示的是value
    book_types = (
        ('Science fiction', '科幻小说'),
        ('Suspense novel', '悬疑小说'),
        ('Romantic novels', '言情小说'),
        ('Other novels', '其他小说')
        )
    book_name = models.CharField(verbose_name='书名', max_length=200, null=False, blank=False)
    pub_date = models.DateField("出版日期")
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="book")
    price = models.FloatField(verbose_name='价格')
    book_type = models.CharField('种类',max_length=50, choices=book_types,default='Other novels')
    
    class Meta:
        db_table = 'book'
        ordering = ('-pub_date',)
    def __str__(self):
        return "{}".format(self.book_name.__str__())

class Author(models.Model):
    name = models.CharField('名字', max_length=32,)
    age = models.PositiveIntegerField()
    sex = models.CharField('性别', max_length=10, choices=(('male','男'),('female','女')), default='male')
    
    class Meta:
        db_table = 'author'
    def __str__(self):
        return "{}".format(self.name)

