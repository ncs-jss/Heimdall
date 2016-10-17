from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=80, blank=False)
	github_name = models.CharField(max_length=80, blank=False)
	alias = models.CharField(max_length=80, default=1)

	def __str__(self):
		return self.

class Data(models.Model):
	user_id = models.ForeignKeyield(User, related_name='user_id')
	attendence_score = models.IntergerField()
	git_commits_score = models.IntergerField()
	discipline_score = models.IntergerField()
	mentor_review = models.CharField(max_length=255)
	#add another review model that carries all the reviews for the user.

class Attendence(models.Model):
	user_id = models.ForeignKeyield(User, related_name='user_id')
	attendence = models.IntergerField()
	created_at = models.DateTimeField(auto_now_add=True)

class Github(models.Model):
	user_id = models.ForeignKeyield(User, related_name='user_id')
	repo_id = models.IntergerField()
	url = models.CharField()
	last_updated = models.DateTimeField()
	commits = models.IntegerField()





