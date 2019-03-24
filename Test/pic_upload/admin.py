from django.contrib import admin
from .models import Picture
# Register your models here.
class PictureAdmin(admin.ModelAdmin):
    list_display= ('id','title','date','image_data')
    # readonly_fields 设置该列不可编辑
    readonly_fields = ('image_data',)
    # 设置带链接的字段
    list_display_links = ('image_data','title',)

admin.site.register(Picture, PictureAdmin)