# Generated by Django 2.2.5 on 2020-09-24 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('pub_date', models.DateField(null=True)),
                ('readcount', models.IntegerField(default=0)),
                ('commentcount', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '图书管理',
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1)),
                ('description', models.CharField(max_length=100, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo')),
            ],
            options={
                'verbose_name': '人员信息',
                'db_table': 'peopleinfo',
            },
        ),
    ]
