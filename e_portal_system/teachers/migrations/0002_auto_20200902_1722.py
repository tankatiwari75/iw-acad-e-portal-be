# Generated by Django 3.1 on 2020-09-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0005_auto_20200902_1535'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendanceuploads',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='attendanceuploads',
            name='date',
        ),
        migrations.RemoveField(
            model_name='attendanceuploads',
            name='student_name',
        ),
        migrations.RemoveField(
            model_name='attendanceuploads',
            name='teacher_name',
        ),
        migrations.RemoveField(
            model_name='resultupload',
            name='student_name',
        ),
        migrations.AddField(
            model_name='attendanceuploads',
            name='class_held',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attendanceuploads',
            name='class_number',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='adminsite.addclassnumber', to_field='class_number'),
        ),
        migrations.AddField(
            model_name='attendanceuploads',
            name='class_present',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attendanceuploads',
            name='teacher_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminsite.teacherregistration', to_field='teacher_unique_id'),
        ),
        migrations.AddField(
            model_name='resultupload',
            name='class_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminsite.addclassnumber', to_field='class_number'),
        ),
        migrations.AddField(
            model_name='resultupload',
            name='pass_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendanceuploads',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsite.studentregistration', to_field='admission_number'),
        ),
        migrations.AlterField(
            model_name='attendanceuploads',
            name='subject_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsite.addsubject', to_field='subject_name'),
        ),
        migrations.AlterField(
            model_name='resultupload',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsite.studentregistration', to_field='admission_number'),
        ),
        migrations.AlterField(
            model_name='resultupload',
            name='subject_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsite.addsubject', to_field='subject_name'),
        ),
        migrations.AlterField(
            model_name='resultupload',
            name='teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsite.teacherregistration', to_field='teacher_unique_id'),
        ),
    ]
