from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
import datetime

def home_view(request):
    #template_name = 'templates/app/home.html' #???
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }


    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages,
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    time = datetime.datetime.now().time()
    current_time = time.strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    directory_contents = os.listdir('.')
    msg = f'Cодержимое рабочей директории: {directory_contents}'
    return HttpResponse(msg)
