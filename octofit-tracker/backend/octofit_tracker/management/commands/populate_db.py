from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Extract database settings
        db_settings = settings.DATABASES['default']
        client = MongoClient(db_settings['HOST'], db_settings['PORT'])
        db = client[db_settings['NAME']]

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create test users
        user1 = {"username": "hero1", "email": "hero1@example.com", "password": "password1"}
        user2 = {"username": "hero2", "email": "hero2@example.com", "password": "password2"}
        db.users.insert_many([user1, user2])

        # Create test teams
        team1 = {"name": "Avengers", "members": [user1["email"], user2["email"]]}
        db.teams.insert_one(team1)

        # Create test activities
        activity1 = {"user": user1["email"], "activity_type": "Running", "duration": "00:30:00"}
        activity2 = {"user": user2["email"], "activity_type": "Cycling", "duration": "01:00:00"}
        db.activity.insert_many([activity1, activity2])

        # Create test leaderboard entries
        leaderboard1 = {"user": user1["email"], "score": 100}
        leaderboard2 = {"user": user2["email"], "score": 200}
        db.leaderboard.insert_many([leaderboard1, leaderboard2])

        # Create test workouts
        workout1 = {"name": "Push-ups", "description": "Do 20 push-ups"}
        workout2 = {"name": "Sit-ups", "description": "Do 30 sit-ups"}
        db.workouts.insert_many([workout1, workout2])

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
