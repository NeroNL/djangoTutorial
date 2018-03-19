from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def currentTime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request):
    print request
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