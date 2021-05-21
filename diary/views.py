from django.shortcuts import render, redirect
from diary.models import Diary
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


def diary_main(request):
    diaries = Diary.objects.all().order_by('-id')
    num = len(diaries)
    ctx = {
        'num': num
    }
    return render(request, 'diary/home.html', ctx)


def diary_list(request):
    diaries = Diary.objects.all().order_by('-id')
    ctx = {
        'diaries': diaries,
    }
    return render(request, 'diary/cover.html', ctx)


def diary_detail(request, pk):
    diary = Diary.objects.get(id=pk)
    ctx = {
        'diary': diary
    }
    return render(request, 'diary/inside.html', ctx)


def diary_create(request):
    if request.method == 'GET':
        return render(request, 'diary/newpage.html')
    else:
        title = request.POST['title']
        content = request.POST['content']

        diary = Diary.objects.create(title=title, content=content)
        pk = diary.id
        diary = Diary.objects.get(id=pk)
        ctx = {
            'diary': diary
        }
        return render(request, 'diary/inside.html', ctx)


def diary_update(request, pk):
    if request.method == 'GET':
        diary = Diary.objects.get(id=pk)
        ctx = {
            'diary': diary
        }
        return render(request, 'diary/edit.html', ctx)
    else:
        title = request.POST['title']
        content = request.POST['content']
        Diary.objects.filter(id=pk).update(title=title, content=content)
        diary = Diary.objects.get(id=pk)
        ctx = {
            'diary': diary
        }
        return render(request, 'diary/inside.html', ctx)


def diary_delete(request, pk):
    if request.method == 'GET':
        return redirect('/diary')
    else:
        diary = Diary.objects.get(id=pk)
        diary.delete()
        return redirect('/diary')