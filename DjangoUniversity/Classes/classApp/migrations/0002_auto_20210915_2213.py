# Generated by Django 3.2.6 on 2021-09-16 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='Course_Number',
            field=models.IntegerField(blank=True, default='', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='Instructor_Name',
            field=models.CharField(blank=True, default='', max_length=75),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='Title',
            field=models.CharField(blank=True, default='', max_length=75),
        ),
    ]
