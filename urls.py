from django.urls import path
from . import views


urlpatterns = [
    path('current_time/', views.get_current_time)
]
