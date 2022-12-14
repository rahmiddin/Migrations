# Generated by Django 4.1.1 on 2022-09-09 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_alter_studteach_student_alter_studteach_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(through='school.StudTeach', to='school.teacher'),
        ),
        migrations.AlterField(
            model_name='studteach',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.student'),
        ),
        migrations.AlterField(
            model_name='studteach',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.teacher'),
        ),
    ]
