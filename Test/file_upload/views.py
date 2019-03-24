from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm, FileUploadModelForm
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat
import os 
import uuid

# Create your views here.
def file_list(request):
    files = File.objects.all().order_by('-id') 
    return render(request, 'file_list.html', {'files':files})

# 普通表单上传文件
def file_upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES) # 提交的文件在请求的Files里
        if form.is_valid(): # 检查表单里的数据是否有效
            upload_metdhod = form.cleaned_data.get('upload_method') # 获取上传的文件类型
            raw_file = form.cleaned_data.get('file') # 获取文件
            new_file = File()
            print (raw_file.name)  #上传时候的文件名 47268c9a5fbbc91b4623b997e040157f.jpg
            new_file.file = handle_uploaded_file(raw_file)
            new_file.upload_method = upload_metdhod
            new_file.save()
            return redirect("/file/")
    else:
        form = FileUploadForm()
    return render(request, 'upload_form.html', {'form': form,'heading': 'Upload files with Regular Form'})

# 手动重命名
def handle_uploaded_file(file):
    # 一点为分界获取后缀名 如 xxx.jpg 分为两部分xxx 和 jpg, 获取jpg
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext) # 随机生成新的文件名
    
    # file path relative to 'media' folder
    file_path = os.path.join('files', file_name)
    print (file_path) # files\38a83105fd.jpg
    absolute_file_path = os.path.join('media', 'files', file_name)
    print (absolute_file_path) # media\files\38a83105fd.jpg
    directory = os.path.dirname(absolute_file_path)
    print (directory) # media\files
    
    # 如果文件夹不存就创建一个
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path

# upload file with modelform
def model_form_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/file/")
    else:
        form = FileUploadModelForm()

    return render(request, 'upload_form.html', {'form': form, 'heading': 'Upload files with Model'})

# # Upload File with ModelForm
# def ajax_form_upload(request):
#     form = FileUploadModelForm()
#     return render(request, 'ajax_upload_form.html', {'form': form, 'heading': 'File Upload with AJAX'})

# # handling AJAX requests
# def ajax_upload(request):
#     if request.method == "POST":
#         form = FileUploadModelForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # Obtain the latest file list
#             files = File.objects.all().order_by('-id')
#             data = []
#             for file in files:
#                 data.append({
#                     "url": file.file.url,
#                     "size": filesizeformat(file.file.size),
#                     "upload_method": file.upload_method,
#                     })
#             return JsonResponse(data, safe=False)
#         else:
#             data = {'error_msg': "Only jpg, pdf and xlsx files are allowed."}
#             return JsonResponse(data)
#     return JsonResponse({'error_msg': 'only POST method accpeted.'})