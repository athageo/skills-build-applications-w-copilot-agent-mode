# Test data for populating the octofit_db database

test_users = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "password123"},
    {"username": "alice_wonder", "email": "alice@example.com", "password": "password123"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["john_doe", "jane_smith"]},
    {"name": "Team Beta", "members": ["alice_wonder"]},
]

test_activities = [
    {"user": "john_doe", "activity_type": "Running", "duration": "00:30:00"},
    {"user": "jane_smith", "activity_type": "Cycling", "duration": "01:00:00"},
    {"user": "alice_wonder", "activity_type": "Swimming", "duration": "00:45:00"},
]

test_leaderboard = [
    {"user": "john_doe", "score": 150},
    {"user": "jane_smith", "score": 200},
    {"user": "alice_wonder", "score": 180},
]

test_workouts = [
    {"name": "Push-ups", "description": "Do 20 push-ups"},
    {"name": "Sit-ups", "description": "Do 30 sit-ups"},
    {"name": "Plank", "description": "Hold a plank for 1 minute"},
]
