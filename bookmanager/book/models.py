from django.db import models

# Create your models here.

"""
1. 继承model.Model 
2. 系统自动添加id 
3. 字段
    字段名(数据表字段名) = model.类型
"""


class BookInfo(models.Model):
    # id 自动创建
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# 人物
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.gender, self.book
