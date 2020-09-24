from django.db import models

# Create your models here.


"""
1.定义属性字段不能用连续的下划线
2.类型 -- mysql的类型
3.选项
    CharField 必须设置max_length
4. 改变表的名称
    默认子应用名类名 
    修改表的名字  
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pub_data = models.DateField(null=True, )
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'bookinfo'  # 修改名字
        verbose_name = '书记管理' # admin 站点管理 了解


class PeopleInfo(models.Model):
    pass
