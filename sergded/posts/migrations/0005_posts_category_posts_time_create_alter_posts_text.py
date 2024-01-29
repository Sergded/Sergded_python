# Generated by Django 4.2.5 on 2023-10-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_posts_int_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
