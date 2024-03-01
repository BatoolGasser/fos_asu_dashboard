from django.contrib import admin
from user.models import *


# Admin Panel Customization
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'student_name', 'enroll_year', 'graduate_year', 'total_warnings_number']
    search_fields = ['student_name']


admin.site.register(Student, StudentAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_id', 'doctor_name']
    search_fields = ['doctor_name']


admin.site.register(Doctor, DoctorAdmin)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['program_id', 'program_name']
    list_filter = ['program_name']


admin.site.register(Program, ProgramAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_id', 'role_name', 'is_decision_maker']
    list_filter = ['role_name', 'is_decision_maker']


admin.site.register(Role, RoleAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'course_name', 'credit_hours', 'level', 'semester']
    list_filter = ['semester', 'level', 'credit_hours']
    search_fields = ['course_code']


admin.site.register(Courses, CoursesAdmin)


class AcademicTimeAdmin(admin.ModelAdmin):
    list_display = ['academic_time_id', 'academic_year_name', 'academic_semester_name', 'academic_year_int',
                    'academic_semester_int']
    list_filter = ['academic_year_name']


admin.site.register(AcademicTime)


class StudentHasCoursesAdmin(admin.ModelAdmin):
    list_display = ["course_code", "student_id", "course_category", "course_type", "grade", "total_marks"]
    list_filter = ["grade", "course_category", "course_type"]
    search_fields = ['course_code']


admin.site.register(StudentHasCourses, StudentHasCoursesAdmin)


class StudentHasProgramAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'program_id', 'academic_time_id']


admin.site.register(StudentHasProgram, StudentHasProgramAdmin)
admin.site.register(StudentHasSemester)
admin.site.register(DoctorTeachCourses)
admin.site.register(ProgramHasCourses)
