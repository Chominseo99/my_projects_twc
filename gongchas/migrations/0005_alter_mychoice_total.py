# Generated by Django 3.2.9 on 2021-11-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gongchas', '0004_auto_20211130_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mychoice',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
