# Generated by Django 2.2 on 2019-04-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190419_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
