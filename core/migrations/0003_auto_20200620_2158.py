# Generated by Django 3.0.7 on 2020-06-20 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200620_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(max_length=800),
        ),
    ]
