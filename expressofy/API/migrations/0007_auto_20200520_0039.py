# Generated by Django 3.0.6 on 2020-05-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20200520_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_dob',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_profession',
            field=models.CharField(max_length=20),
        ),
    ]
