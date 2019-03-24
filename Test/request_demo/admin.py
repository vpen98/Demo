from django.contrib import admin
from .models import Book,Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','sex')
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name',"author",'book_type','price')
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)