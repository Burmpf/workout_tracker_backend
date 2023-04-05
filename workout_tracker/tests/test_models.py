from django.test import TestCase
from django.contrib.auth.models import User
from workout_tracker.models import DailyLog, Exercise, MuscleGroup


class DailyLogModelTest(TestCase):
    def test_create_daily_log(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        daily_log = DailyLog.objects.create(user=user, date="2022-10-01", weight=150, sleep_hours=8, mood=3)
        self.assertEqual(daily_log.date, "2022-10-01")
        self.assertEqual(daily_log.weight, 150)
        self.assertEqual(daily_log.sleep_hours, 8)
        self.assertEqual(daily_log.mood, 3)


class ExerciseModelTest(TestCase):
    def test_create_exercise(self):
        muscle_group = MuscleGroup.objects.create(name="Chest")
        exercise = Exercise.objects.create(exercise_name="Bench Press", muscle_group=muscle_group)
        self.assertEqual(exercise.exercise_name, "Bench Press")
        self.assertEqual(exercise.muscle_group, muscle_group)
