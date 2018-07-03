from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from artapp.models import book, Art


# Create your views here.
def index(request):
    # 请求路径和请求方法
    # print(request.path, request.method)
    # # 请求头的元信息和GET请求参数(查询参数)
    # print(request.META, request.GET)
    # # POST请求参数(表单参数)
    # print(request.POST)
    # return HttpResponse('<h1>您好</h1>')
    # return JsonResponse({'name':'lisi', 'age':20})
    return render(request, 'art/list.html', context={'arts': Art.objects.all(), 'tags': book.objects.all()})


def add_tags(request):
    if request.method == 'GET':
        id1 = ''
        title = ''
        if request.GET.get('id'):
            id1 = request.GET.get('id')
            title = book.objects.get(id=id1).title
        return render(request, 'art/edit_tags.html', {'id': id1, 'title': title})
    else:
        if request.POST.get('id'):
            id1 = request.POST.get('id')
            tag = book.objects.get(id=id1)
        else:
            tag = book()
        title = request.POST.get('title')
        tag.title = title
        tag.save()
        return redirect('/art/tags_list/1/')


def tag_list(request, page_num):
    tags = book.objects.all()
    paginator = Paginator(tags, 3)
    page = paginator.page(page_num)
    data = {
        'page_range': paginator.page_range,
        'page': page,
    }
    return render(request, 'art/tags_list.html', context={'tags': data})


def delete_tag(request):
    id1 = request.GET.get('id')
    tag = book.objects.filter(id=id1)
    if tag.exists():
        tag.delete()
    return redirect('/art/tags_list/1/')

