# Generated by Django 2.2 on 2019-04-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190427_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatechat',
            name='profile1',
        ),
        migrations.RemoveField(
            model_name='privatechat',
            name='profile2',
        ),
        migrations.AddField(
            model_name='privatechat',
            name='profile',
            field=models.ManyToManyField(to='main.Profile'),
        ),
    ]
