from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        for user_data in test_users:
            user, created = User.objects.get_or_create(**user_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'User created: {user.username}'))

        # Populate teams
        for team_data in test_teams:
            members = team_data.pop('members')
            team, created = Team.objects.get_or_create(**team_data)
            if created:
                team.members = list(User.objects.filter(username__in=members))
                team.save()
                self.stdout.write(self.style.SUCCESS(f'Team created: {team.name}'))

        # Populate activities
        for activity_data in test_activities:
            activity, created = Activity.objects.get_or_create(**activity_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Activity created: {activity.activity_type} for user {activity.user.username}'))

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            leaderboard, created = Leaderboard.objects.get_or_create(**leaderboard_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Leaderboard entry created for user {leaderboard.user.username} with score {leaderboard.score}'))

        # Populate workouts
        for workout_data in test_workouts:
            workout, created = Workout.objects.get_or_create(**workout_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Workout created: {workout.name}'))
