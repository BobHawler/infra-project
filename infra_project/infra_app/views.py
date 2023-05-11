from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Получилось ведь?')


def second_page(request):
    return HttpResponse('А это вторая страница!')
