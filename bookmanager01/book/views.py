from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from book.models import BookInfo, PeopleInfo


def index(request):
    return HttpResponse('ok')



# # 聚合函数
# from django.db.models import Sum, Max, Min, Avg, Count
# BookInfo.objects.aggregate(Sum('readcount'))  # 聚合--总数
# BookInfo.objects.all().order_by('-readcount')  # 排序
# # 两个表的操作
# book = BookInfo.objects.get(id=1)
# book.peopleinfo_set.all()
#
# person = PeopleInfo.objects.get(id=1)
# person.book.name
# person.book.readcount
#
# BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
# BookInfo.objects.filter(peopleinfo__name='郭靖')
#
# PeopleInfo.objects.filter(book__name='天龙八部')
# PeopleInfo.objects.filter(book__name__exact='天龙八部'
#                                      ''
#                                             '')