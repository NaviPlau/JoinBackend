# Generated by Django 5.1.4 on 2024-12-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_auth', '0002_userprofile_phone_userprofile_selected_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. Must contain exactly two words.', max_length=150, unique=True),
        ),
    ]
