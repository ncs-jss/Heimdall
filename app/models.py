from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=80, blank=False)
	github_name = models.CharField(max_length=80, blank=False)
	alias = models.CharField(max_length=80, default=1)

	def __str__(self):
		return self.username

class Data(models.Model):
	user = models.ForeignKey(User, related_name='+')
	attendence_score = models.IntegerField()
	git_commits_score = models.IntegerField()
	discipline_score = models.IntegerField()
	mentor_review = models.CharField(max_length=255)
	#add another review model that carries all the reviews for the user.

class Attendence(models.Model):
	user = models.ForeignKey(User, related_name='+')
	attendence = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

class Github(models.Model):
	user = models.ForeignKey(User, related_name='+')
	repo_id = models.IntegerField()
	url = models.CharField(max_length=255)
	last_updated = models.DateTimeField()
	commits = models.IntegerField()





