from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
    test1 = Test(name='w3cschool.cn')
    test1.save()
    return HttpResponse("<p>Success!</p>")