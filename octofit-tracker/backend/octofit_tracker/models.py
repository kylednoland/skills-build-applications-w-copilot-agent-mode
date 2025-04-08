from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField('User')

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()