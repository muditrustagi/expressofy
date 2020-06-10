# Generated by Django 3.0.6 on 2020-05-19 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('joined_on', models.DateTimeField(db_column='user_joined_on')),
                ('profile_image', models.ImageField(db_column='user_profile_image', upload_to='')),
                ('name', models.CharField(db_column='user_name', max_length=40)),
                ('bio', models.CharField(db_column='user_bio', max_length=100)),
                ('gender', models.CharField(db_column='user_gender', max_length=20)),
                ('phone_number', models.CharField(db_column='user_phone_number', max_length=20)),
                ('profession', models.CharField(db_column='user_profession', max_length=20)),
                ('email', models.EmailField(db_column='user_email', max_length=254)),
                ('dob', models.DateTimeField(db_column='user_dob')),
                ('fcoin', models.CharField(db_column='user_fcoin', max_length=20)),
                ('state', models.IntegerField(db_column='user_state', default=1)),
                ('interests', models.CharField(db_column='user_interests', max_length=100)),
                ('is_premium', models.IntegerField(db_column='user_is_premium', default=0)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]