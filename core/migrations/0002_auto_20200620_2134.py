# Generated by Django 3.0.7 on 2020-06-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_text',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='answer_to_question',
            new_name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
