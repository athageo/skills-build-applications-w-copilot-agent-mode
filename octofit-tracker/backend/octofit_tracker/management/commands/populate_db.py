from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

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
                team.members.set(User.objects.filter(username__in=members))
                team.save()
                self.stdout.write(self.style.SUCCESS(f'Team created: {team.name}'))

        # Populate activities
        for activity_data in test_activities:
            user = User.objects.get(username=activity_data.pop('user'))
            activity, created = Activity.objects.get_or_create(user=user, **activity_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Activity created: {activity.activity_type} for {user.username}'))

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            user = User.objects.get(username=leaderboard_data.pop('user'))
            leaderboard, created = Leaderboard.objects.get_or_create(user=user, **leaderboard_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Leaderboard entry created for {user.username}'))

        # Populate workouts
        for workout_data in test_workouts:
            workout, created = Workout.objects.get_or_create(**workout_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Workout created: {workout.name}'))
