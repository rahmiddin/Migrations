# Generated by Django 4.1.1 on 2022-09-08 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_rename_students_studteach_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='student', through='school.StudTeach', to='school.teacher'),
        ),
        migrations.AlterField(
            model_name='studteach',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student'),
        ),
        migrations.AlterField(
            model_name='studteach',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher'),
        ),
    ]
