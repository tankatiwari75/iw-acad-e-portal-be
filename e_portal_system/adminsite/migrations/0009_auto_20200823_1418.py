# Generated by Django 3.1 on 2020-08-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0008_auto_20200823_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directmessagemodel',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
