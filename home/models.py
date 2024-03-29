from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    doctor_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        null=False
    )
    doctor_name = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'Doctor'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.CharField(primary_key=True, max_length=50)
    student_name = models.CharField(max_length=200, null=True)
    enroll_year = models.DateField(null=True)
    graduate_year = models.DateField(null=True, blank=True)
    total_warnings_number = models.IntegerField(null=True)
    supervisor_user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='supervised_students', null=True)

    class Meta:
        db_table = 'Student'


class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        null=False
    )
    role_name = models.CharField(max_length=100, null=True)
    is_decision_maker = models.BooleanField(null=True)

    class Meta:
        db_table = 'Role'


class Program(models.Model):
    program_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        null=False
    )
    program_name = models.CharField(max_length=50, null=True)
    students = models.ManyToManyField('Student', through='StudentHasProgram')

    class Meta:
        db_table = 'Program'


class Courses(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=70, null=True, blank=True)
    credit_hours = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True)
    semester = models.CharField(max_length=10, null=True)
    students = models.ManyToManyField('Student', through='StudentHasCourses')
    programs = models.ManyToManyField('Program', through='ProgramHasCourses')
    supervised_program = models.ForeignKey(Program, models.CASCADE, related_name='program_supervise_courses')
    doctors = models.ManyToManyField('Doctor', through='DoctorTeachCourses')

    class Meta:
        db_table = 'Courses'


class AcademicTime(models.Model):
    academic_time_id = models.IntegerField(primary_key=True)
    academic_year_name = models.CharField(max_length=20)
    academic_semester_name = models.CharField(max_length=20)
    academic_year_int = models.IntegerField()
    academic_semester_int = models.IntegerField()
    students = models.ManyToManyField('Student', through='StudentHasSemester')

    class Meta:
        db_table = 'AcademicTime'


class DoctorTeachCourses(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    course_code = models.ForeignKey(Courses,
                                       on_delete=models.CASCADE,
                                       related_name='doctor_teach_courses',
                                       null=True,
                                       db_column="course_code"
                                       )
    academic_time = models.ForeignKey(AcademicTime, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'DoctorTeachCourses'
        unique_together = ['doctor', 'course_code', 'academic_time']


class ProgramHasCourses(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, db_column="course_code")
    mandatory_type = models.BooleanField(null=True)

    class Meta:
        db_table = 'ProgramHasCourses'
        unique_together = ['program', 'course_code']


class StudentHasCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, name='course_code',
                               db_column="course_code")
    course_category = models.CharField(max_length=30, null=True, blank=True)
    course_type = models.CharField(max_length=20, null=True, blank=True)
    grade = models.CharField(max_length=2, null=True)
    oral = models.IntegerField(null=True, blank=True)
    practical = models.IntegerField(null=True, blank=True)
    total_marks = models.IntegerField(null=True, blank=True)
    year_work_marks = models.IntegerField(null=True, blank=True)
    final_marks = models.IntegerField(null=True, blank=True)
    academic_time = models.ForeignKey(AcademicTime, models.CASCADE)

    class Meta:
        db_table = 'StudentHasCourses'
        unique_together = ['student', 'course_code', 'academic_time']


class StudentHasProgram(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)
    academic_time = models.ForeignKey(AcademicTime, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'StudentHasProgram'
        unique_together = ['student', 'program', 'academic_time']


class StudentHasSemester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    academic_time = models.ForeignKey(AcademicTime, models.CASCADE, null=True)
    cummulative_gpa = models.FloatField(null=True, blank=True)
    passed_hours = models.IntegerField(null=True, blank=True)
    hours_in_progress = models.IntegerField(null=True, blank=True)
    warnings_number = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    semester_gpa = models.FloatField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'StudentHasSemester'
        unique_together = ['student', 'academic_time']
