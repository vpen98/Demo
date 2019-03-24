from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]
    
admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

# class ArticleAdmin(admin.ModelAdmin):

#     '''设置列表可显示的字段'''
#     list_display = ('title', 'author',  'status', 'mod_date',)

#     '''设置过滤选项'''
#     list_filter = ('status', 'pub_date', )

#     '''每页显示条目数'''
#     list_per_page = 5

#     '''设置可编辑字段'''
#     list_editable = ('status',)

#     '''按日期月份筛选'''
#     date_hierarchy = 'pub_date'

#     '''按发布日期排序'''
#     ordering = ('-mod_date',)

# admin.site.register(Article, ArticleAdmin)
#  list_display_links和search_fields。
#  前者设置带链接的字段，比如本例中带链接的字段为('title'), 
#  后者设置可以搜索的字段，如('title', 'body')，
#  方便快速查询需要修改的数据表条目。
# 注意: list_display不能用在多对多字段上哦。