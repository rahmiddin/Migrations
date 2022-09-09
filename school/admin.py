from django.contrib import admin

from .models import Student, Teacher,StudTeach


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(StudTeach)
class StudTeachAdmin(admin.ModelAdmin):
    pass