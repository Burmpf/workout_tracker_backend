from django.urls import path
from . import views

# Define URL patterns for workout_tracker API
urlpatterns = [
    # MuscleGroup API endpoints
    path('musclegroups/', views.MuscleGroupList.as_view(), name='musclegroup_list'),
    path('musclegroups/<int:pk>/', views.MuscleGroupDetail.as_view(), name='musclegroup_detail'),

    # Exercise API endpoints
    path('exercises/', views.ExerciseList.as_view(), name='exercise_list'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercise_detail'),

    # DailyLog API endpoints
    path('dailylogs/', views.DailyLogList.as_view(), name='dailylog_list'),
    path('dailylogs/<int:pk>/', views.DailyLogDetail.as_view(), name='dailylog_detail'),

    # ExerciseLog API endpoints
    path('exerciselogs/', views.ExerciseLogList.as_view(), name='exerciselog_list'),
    path('exerciselogs/<int:pk>/', views.ExerciseLogDetail.as_view(), name='exerciselog_detail'),
]