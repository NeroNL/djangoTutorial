# -*- coding: utf-8 -*-


from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf


# form
def search_form(request):
    return render_to_response('search_form.html')


# receive request data
def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'Search Content:' + request.GET['q'].encode('utf-8')
    else:
        message = 'You submitted an empty form'
    return HttpResponse(message)


def search_post(request):
    ctx={}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post_form.html", ctx)
