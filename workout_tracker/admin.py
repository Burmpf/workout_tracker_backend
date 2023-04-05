from django.contrib import admin
from .models import MuscleGroup, Exercise, DailyLog, ExerciseLog

# Register your models here.

admin.site.register(MuscleGroup)
admin.site.register(Exercise)
admin.site.register(DailyLog)
admin.site.register(ExerciseLog)
