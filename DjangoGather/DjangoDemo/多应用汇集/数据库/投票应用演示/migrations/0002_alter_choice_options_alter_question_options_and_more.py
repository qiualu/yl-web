# Generated by Django 5.0.7 on 2025-01-14 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('投票应用演示', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': '选项', 'verbose_name_plural': '选项'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '问题', 'verbose_name_plural': '问题'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='选项的文本内容'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='投票应用演示.question', verbose_name='关联问题'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='票数'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布日期和时间'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='问题的文本内容'),
        ),
    ]
