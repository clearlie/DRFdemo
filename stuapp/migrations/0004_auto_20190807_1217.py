# Generated by Django 2.2.1 on 2019-08-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0003_auto_20190805_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='aname',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
