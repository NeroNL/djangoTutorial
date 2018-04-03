import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def currentTime(request):
    now = datetime.datetime.now()
    c = {}
    c['current_time'] = now
    return render_to_response('currentTime.html', c)


def hours_ahead(request):
    path = request.path
    start = path.find('plus/')+5
    end = path.find('/', start)
    offset = path[start:end]
    try:
        offset = int(offset)
    except ValueError():
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours, it will be %s</body></html>" % (offset, dt)
    return HttpResponse(html)


def meta_data(request):
    values = request.META.items()
    values.sort()
    meta = {'values': values}
    return render_to_response('requestMeta.html', meta)


def print_article(request, year, month, day):
    print month, day, year
    html = "<html><body>This article you are looking for is published in %s/%s/%s</body></html>" % (month, day, year)
    return HttpResponse(html)
