# Generated by Django 3.1 on 2020-09-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherregistration',
            name='teacher_id',
            field=models.IntegerField(unique=True),
        ),
    ]