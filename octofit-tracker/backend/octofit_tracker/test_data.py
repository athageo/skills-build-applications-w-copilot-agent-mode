# Test data for populating the octofit_db database

test_users = [
    {"username": "hero1", "email": "hero1@example.com", "password": "password1"},
    {"username": "hero2", "email": "hero2@example.com", "password": "password2"}
]

test_teams = [
    {"name": "Avengers", "members": ["hero1@example.com", "hero2@example.com"]}
]

test_activities = [
    {"user": "hero1@example.com", "activity_type": "Running", "duration": "00:30:00"},
    {"user": "hero2@example.com", "activity_type": "Cycling", "duration": "01:00:00"}
]

test_leaderboard = [
    {"user": "hero1@example.com", "score": 100},
    {"user": "hero2@example.com", "score": 200}
]

test_workouts = [
    {"name": "Push-ups", "description": "Do 20 push-ups"},
    {"name": "Sit-ups", "description": "Do 30 sit-ups"}
]
