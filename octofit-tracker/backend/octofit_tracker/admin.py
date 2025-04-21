from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Registering models for admin interface
admin.site.register(Leaderboard)
admin.site.register(Workout)
