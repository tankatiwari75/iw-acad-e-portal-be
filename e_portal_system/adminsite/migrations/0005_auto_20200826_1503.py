# Generated by Django 3.1 on 2020-08-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0004_auto_20200823_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directmessagemodel',
            name='attachment',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]