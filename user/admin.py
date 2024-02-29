from django.contrib import admin
from user.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Doctor)
admin.site.register(Program)
admin.site.register(Role)
admin.site.register(Courses)
admin.site.register(AcademicTime)
admin.site.register(StudentHasCourses)
admin.site.register(StudentHasProgram)
admin.site.register(StudentHasSemester)
admin.site.register(DoctorTeachCourses)
admin.site.register(ProgramHasCourses)
