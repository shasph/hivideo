# Generated by Django 3.2.3 on 2021-07-23 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_auto_20210723_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='v_content',
            new_name='v_file',
        ),
    ]