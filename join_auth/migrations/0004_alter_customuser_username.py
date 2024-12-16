# Generated by Django 5.1.4 on 2024-12-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_auth', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text='Required. Must contain exactly two words.', max_length=150),
        ),
    ]
