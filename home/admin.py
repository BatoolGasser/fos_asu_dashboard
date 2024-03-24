from django.contrib import admin
from django.contrib.auth import get_user_model
from home.models import *

# Admin Panel Customization
User = get_user_model()


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_id', 'student_name', 'enroll_year', 'graduate_year', 'total_warnings_number']
    search_fields = ['student_name']


admin.site.register(Student, StudentAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'doctor_id', 'doctor_name']
    search_fields = ['doctor_name']


admin.site.register(Doctor, DoctorAdmin)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['program_id', 'program_name']
    list_filter = ['program_name']


admin.site.register(Program, ProgramAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'role_name', 'is_decision_maker']
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
    list_filter = ['academic_year_name', 'academic_semester_name', 'academic_year_int']


admin.site.register(AcademicTime, AcademicTimeAdmin)


class StudentHasCoursesAdmin(admin.ModelAdmin):
    def get_student_name(self, obj):
        return obj.student.student_name

    get_student_name.short_description = 'Student Name'

    def get_academic_time(self, obj):
        return obj.academic_time.academic_year_name

    get_academic_time.short_description = 'Academic Time'

    def get_semester(self, obj):
        return obj.academic_time.academic_semester_name

    get_semester.short_description = 'Semester'

    list_display = ['get_student_name', "course_code_id", "get_academic_time", "get_semester", "grade", "total_marks"]
    list_filter = ["grade", "course_category", "course_type"]
    search_fields = ['course_code']


admin.site.register(StudentHasCourses, StudentHasCoursesAdmin)


class StudentHasProgramAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'program_id', 'academic_time_id']


admin.site.register(StudentHasProgram, StudentHasProgramAdmin)


class StudentHasSemesterAdmin(admin.ModelAdmin):
    def get_student_name(self, obj):
        return obj.student.student_name

    get_student_name.short_description = 'Student Name'

    def get_academic_time(self, obj):
        return obj.academic_time.academic_year_name

    get_academic_time.short_description = 'Academic Time'

    def get_semester(self, obj):
        return obj.academic_time.academic_semester_name

    get_semester.short_description = 'Semester'

    list_display = ["get_student_name", "get_academic_time", "get_semester","semester_gpa", "cummulative_gpa",
                    "level", "rank"]
    list_filter = ["student_id"]


admin.site.register(StudentHasSemester, StudentHasSemesterAdmin)


class DoctorTeachCoursesAdmin(admin.ModelAdmin):
    def get_doctor_name(self, obj):
        return obj.doctor.doctor_name

    get_doctor_name.short_description = 'Doctor Name'

    def get_course_code(self, obj):
        return obj.course_code.course_code

    get_course_code.short_description = 'Course Code'

    def get_academic_time(self, obj):
        return obj.academic_time.academic_year_name

    get_academic_time.short_description = 'Academic Time'

    def get_semester(self, obj):
        return obj.academic_time.academic_semester_name

    get_semester.short_description = 'Semester'

    list_display = ['get_doctor_name', 'get_course_code', 'get_academic_time', 'get_semester']
    list_filter = ['doctor__doctor_name']


admin.site.register(DoctorTeachCourses, DoctorTeachCoursesAdmin)

admin.site.register(ProgramHasCourses)
