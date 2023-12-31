# Generated by Django 4.2.3 on 2023-07-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_comment_post_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/videos/'),
        ),
    ]
