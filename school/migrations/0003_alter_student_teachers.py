# Generated by Django 4.1.1 on 2022-09-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_alter_student_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', through='school.StudTeach', to='school.teacher'),
        ),
    ]
