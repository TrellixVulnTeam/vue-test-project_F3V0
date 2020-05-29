# Generated by Django 3.0.4 on 2020-04-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='名称')),
                ('description', models.CharField(default='', max_length=2000, verbose_name='描述')),
                ('service_id', models.IntegerField(default=0, verbose_name='服务id')),
                ('context', models.CharField(default='{}', max_length=5000, verbose_name='内容')),
            ],
        ),
    ]
