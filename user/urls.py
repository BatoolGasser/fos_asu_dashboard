from django.urls import path
from . import views
from .views import *

app_name = "user"

urlpatterns = [
    path('home/', views.home, name="user"),

    path('rest/fbv/<str:pk>', views.FBV_pk),

    path('api/data/get_data_pk/<str:pk>', views.get_data_pk)
]