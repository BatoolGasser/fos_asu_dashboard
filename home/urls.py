from django.urls import path
from . import views
from .views import *
from home.dash_apps import student_performance
from home.dash_apps import student_register

app_name = "home"

urlpatterns = [
    # path('home/', views.home, name="home"),

    path('rest/fbv/<str:pk>', views.FBV_pk),

    path('api/data/get_data_pk/<str:pk>', views.get_data_pk),

    path('register', views.student_register_display, name='student_register'),
    path('performance', views.student_performance_display, name='student_performance'),

    path('/<str:pk>', views.get_student_data)

]