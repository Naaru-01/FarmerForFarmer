# Generated by Django 3.1 on 2020-09-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Crop Protection', 'Crop Protection'), ('Seeds', 'Seeds'), ('Irrigation', 'Irrigation'), ('Climate', 'Climate'), ('Soil/Land', 'Soil/Land'), ('Others', 'Others')], max_length=50),
        ),
    ]