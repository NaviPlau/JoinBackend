# Generated by Django 5.1.4 on 2024-12-13 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join_auth', '0008_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='selected',
        ),
    ]