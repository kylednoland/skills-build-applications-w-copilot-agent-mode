from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor'),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers'),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(id=ObjectId(), name='Blue Team')
        team1.save()
        team1.members.set(users[:3])

        team2 = Team(id=ObjectId(), name='Gold Team')
        team2.save()
        team2.members.set(users[3:])

        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], type='Cycling', duration=60, date='2025-04-08'),
            Activity(id=ObjectId(), user=users[1], type='Crossfit', duration=120, date='2025-04-07'),
            Activity(id=ObjectId(), user=users[2], type='Running', duration=90, date='2025-04-06'),
            Activity(id=ObjectId(), user=users[3], type='Strength', duration=30, date='2025-04-05'),
            Activity(id=ObjectId(), user=users[4], type='Swimming', duration=75, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=team1, score=300),
            Leaderboard(id=ObjectId(), team=team2, score=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Cycling Training', description='Road cycling event training', duration=60),
            Workout(id=ObjectId(), name='Crossfit', description='Crossfit competition training', duration=120),
            Workout(id=ObjectId(), name='Running Training', description='Marathon training', duration=90),
            Workout(id=ObjectId(), name='Strength Training', description='Strength training', duration=30),
            Workout(id=ObjectId(), name='Swimming Training', description='Swimming competition training', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
