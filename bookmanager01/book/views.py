from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from book.models import BookInfo, PeopleInfo


def index(request):
    return HttpResponse('ok')


#################################新增数据
book = BookInfo(
    name='django',
    pub_date='2000-01-1',
    readcount=10
)
book.save()

# 方式2
book1 = BookInfo.objects.create(
    name='django1',
    pub_date='2000-01-1',
    readcount=10
)
book1.save()
#################################修改数据
# 方式一
book = BookInfo.objects.get(id=1)
book.name = '射雕英雄传---1'
book.save()

# 方法二
BookInfo.objects.filter(id=8).update(name='爬虫', commentcount=666)

# 删除数据
BookInfo.objects.get(id=8).delete()
BookInfo.objects.filter(name='django').delete()
# 查询数据
BookInfo.objects.get(id=1)
BookInfo.objects.get(pk=1)

BookInfo.objects.all()
BookInfo.objects.count()

# 查询编号为1的图书
BookInfo.objects.get(id=1)
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])

# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')
from django.db.models import F, Q

BookInfo.objects.filter(readcount__gt=F('commentcount'))
BookInfo.objects.filter(readcount__gt=F('commentcount') * 2)

BookInfo.objects.filter(readcount__gt=20, id__lt=3)
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)

BookInfo.objects.filter(Q(readcount__gt=20))

BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

BookInfo.objects.filter(~Q(id=3))
BookInfo.objects.exclude(id=3)
# # 聚合函数
from django.db.models import Sum, Max, Min, Avg, Count

BookInfo.objects.aggregate(Sum('readcount'))
BookInfo.objects.aggregate(Max('readcount'))
BookInfo.objects.aggregate(Min('readcount'))
BookInfo.objects.aggregate(Avg("readcount"))
BookInfo.objects.aggregate(Count('readcount'))
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
#            '')

# 排序
BookInfo.objects.all().order_by('readcount')

