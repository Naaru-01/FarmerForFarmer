# Generated by Django 3.1 on 2020-09-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200918_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Question',
            new_name='Select_Question',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='Select_category',
        ),
    ]