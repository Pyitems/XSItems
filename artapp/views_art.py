from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import Q
from django.shortcuts import render, redirect

from artapp.models import book, Art


# 文章请求相关的处理函数
def art_edit(request):
    if request.method == 'GET':
        return render(request, 'art/edit_art.html', {'tags': book.objects.all()})
    else:
        title = request.POST.get('title').strip()
        author = request.POST.get('author').strip()
        summary = request.POST.get('summary').strip()
        tag_id = request.POST.get('tag').strip()
        art_img: InMemoryUploadedFile = request.FILES.get('artImg')
        # 验证数据
        error = {}
        if not title:
            error['title'] = '标题不能为空'
        elif len(title) > 20:
            error['title'] = '长度不能超过20个字符'
        if not author:
            error['author'] = '作者不能为空'
        elif len(title) > 20:
            error['author'] = '长度不能超过20个字符'
        if len(error) > 0:
            return render(request, 'art/edit_art.html', {'tags': book.objects.all(), 'error': error})
        # 保存数据
        art = Art()
        art.title = title
        art.summary = summary
        art.author = author
        art.image = art_img
        art.tags_id = tag_id
        art.save()
        return redirect('/art/index/')


def search(request):
    searchkey = request.POST.get('searchkey')
    arts = Art.objects.filter(Q(title__contains=searchkey) | Q(author__contains=searchkey))

    return render(request, 'art/list_search.html', {'arts': arts})
