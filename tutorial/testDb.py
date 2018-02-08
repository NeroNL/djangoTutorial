from django.http import HttpResponse
from TestModel.models import Test


def testdb1(request):
    test1 = Test(name='w3cschool.cn')
    test1.save()
    return HttpResponse("<p>Success!</p>")


def testdb2(request):
    response = ""
    response1 = ""
    # this equals to "select * from"
    list = Test.objects.all()
    # filter() == where
    response2 = Test.objects.filter(id=1)
    # select single target
    response3 = Test.objects.get(id=1)
    # offset 0 limit 2
    Test.objects.order_by('name')[0:2]
    # re-order objects in db by id
    Test.objects.order_by("id")
    # select * from Test where name='w3cschool.cn' order by id;
    Test.objects.filter(name='w3cschool.cn').order_by("id")
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")