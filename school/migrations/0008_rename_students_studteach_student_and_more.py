# Generated by Django 4.1.1 on 2022-09-08 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_alter_student_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studteach',
            old_name='students',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='studteach',
            old_name='teachers',
            new_name='teacher',
        ),
    ]