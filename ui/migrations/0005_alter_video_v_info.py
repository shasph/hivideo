# Generated by Django 3.2.3 on 2021-08-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0004_video_v_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='v_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
