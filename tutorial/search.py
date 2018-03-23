# -*- coding: utf-8 -*-


from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf

from BookList.models import Book


# form
def search_form(request):
    return render_to_response('search_form.html')


# receive request data
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html.html',
                                      {'books': books, 'query': q})
    return render_to_response('search_form.html.html',
                              {'errors': errors})


def search_post(request):
    ctx={}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post_form.html", ctx)
