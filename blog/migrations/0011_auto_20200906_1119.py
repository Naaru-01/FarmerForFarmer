# Generated by Django 3.1 on 2020-09-06 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='category',
        ),
    ]
