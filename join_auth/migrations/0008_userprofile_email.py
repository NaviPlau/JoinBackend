# Generated by Django 5.1.4 on 2024-12-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_auth', '0007_alter_userprofile_initials_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
