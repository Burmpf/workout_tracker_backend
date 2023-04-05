from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from workout_tracker.models import DailyLog, Exercise, MuscleGroup


class DailyLogTrackerViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.daily_log = DailyLog.objects.create(user=self.user, date="2022-10-01", weight=150, sleep_hours=8, mood=3)

    def test_daily_log_list_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('dailylog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2022-10-01")

    def test_daily_log_detail_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('dailylog_detail', args=[str(self.daily_log.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2022-10-01")
        self.assertContains(response, "150")
