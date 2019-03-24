from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author
from django.db.models import Q,F
# Create your views here.
def requestdemo(request):
    user = request.user
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknow') # 如果获取不了值，就返回unknow
    ip = request.META['REMOTE_ADDR']
    context = {'user':user, 'user_agent':user_agent,'ip':ip}
    return render(request, 'demo.html', context)
    
    # values = request.META.items()
    # html = []
    # for k,v in values:
    #     html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))
def Testfinddemo(request):
    return render(request,'testfind.html')


