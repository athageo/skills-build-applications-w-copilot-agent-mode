from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        for user_data in test_users:
            user = User.objects.create(
                _id=user_data['_id'],
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )
            self.stdout.write(self.style.SUCCESS(f'User created: {user.username}'))

        # Populate teams
        for team_data in test_teams:
            team = Team.objects.create(
                _id=team_data['_id'],
                name=team_data['name']
            )
            team.members.set(User.objects.filter(_id__in=team_data['members']))
            self.stdout.write(self.style.SUCCESS(f'Team created: {team.name}'))

        # Populate activities
        for activity_data in test_activities:
            activity = Activity.objects.create(
                _id=activity_data['_id'],
                user=User.objects.get(_id=activity_data['user']),
                activity_type=activity_data['activity_type'],
                duration=activity_data['duration']
            )
            self.stdout.write(self.style.SUCCESS(f'Activity created: {activity.activity_type} for user {activity.user.username}'))

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            leaderboard = Leaderboard.objects.create(
                _id=leaderboard_data['_id'],
                user=User.objects.get(_id=leaderboard_data['user']),
                score=leaderboard_data['score']
            )
            self.stdout.write(self.style.SUCCESS(f'Leaderboard entry created for user {leaderboard.user.username} with score {leaderboard.score}'))

        # Populate workouts
        for workout_data in test_workouts:
            workout = Workout.objects.create(
                _id=workout_data['_id'],
                name=workout_data['name'],
                description=workout_data['description']
            )
            self.stdout.write(self.style.SUCCESS(f'Workout created: {workout.name}'))
