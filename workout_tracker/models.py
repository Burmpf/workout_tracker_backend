from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# The MuscleGroup model represents a group of muscles targeted by an exercise
class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The Exercise model represents a single exercise and the muscle group it targets
class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.exercise_name

# The DailyLog model represents a user's daily log entry, including date, weight, sleep, and mood
class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    sleep_hours = models.IntegerField()
    mood = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"

# The ExerciseLog model represents the details of an exercise performed on a specific day,
# including the daily log it belongs to, the exercise, sets, reps, and weight used
class ExerciseLog(models.Model):
    daily_log = models.ForeignKey(DailyLog, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.daily_log} - {self.exercise.exercise_name}"
