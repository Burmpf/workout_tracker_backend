# Workout Tracker Backend

This is the backend for the Workout Tracker application, which is a RESTful API built using Django and Django Rest Framework. The API provides endpoints for managing users, exercises, and daily logs of workouts.

## Features

- User authentication with Auth0
- CRUD operations for Muscle Groups, Exercises, Daily Logs, and Exercise Logs
- List and detail views for each model
- Pagination for list views

## Requirements

- Python 3.10
- Django 4.1.0
- Django Rest Framework 3.13.0
- djangorestframework-simplejwt 5.1.0
- Auth0 for authentication

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/yourusername/workout_tracker_backend.git
cd workout_tracker_backend
```

2. Create a virtual environment and activate it

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Run the database migrations

```bash
python manage.py migrate
```

5. Create a `.env` file in the project root directory with the following environment variables:

```
SECRET_KEY=<your_secret_key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
AUTH0_DOMAIN=<your_auth0_domain>
API_IDENTIFIER=<your_api_identifier>
```

6. Run the development server

```
python manage.py runserver
```

The API should now be running at `http://localhost:8000/`.

## API Endpoints

- MuscleGroup API endpoints
  - `/musclegroups/` (List and create muscle groups)
  - `/musclegroups/<int:pk>/` (Retrieve, update, and delete a muscle group)

- Exercise API endpoints
  - `/exercises/` (List and create exercises)
  - `/exercises/<int:pk>/` (Retrieve, update, and delete an exercise)

- DailyLog API endpoints
  - `/dailylogs/` (List and create daily logs)
  - `/dailylogs/<int:pk>/` (Retrieve, update, and delete a daily log)

- ExerciseLog API endpoints
  - `/exerciselogs/` (List and create exercise logs)
  - `/exerciselogs/<int:pk>/` (Retrieve, update, and delete an exercise log)
