from django.db import models

class Presets(models.Model):
	user_id = models.PositiveSmallIntegerField()
	p_length = models.PositiveSmallIntegerField()
	is_letter = models.BooleanField()
	is_digit = models.BooleanField()
	is_symbol = models.BooleanField()
	p_case = models.CharField(max_length=10)
	is_unique = models.BooleanField()
	no_of_results = models.PositiveSmallIntegerField()
	preset_title = models.CharField(max_length=30)

class Tips(models.Model):
	user_name = models.CharField(max_length=20)
	tips = models.TextField()

