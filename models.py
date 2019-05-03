from django.db import models
class Admin(models.Model):
	log = models.CharField(max_length=20)
	pas = models.CharField(max_length=20)
	nam = models.CharField(max_length=20)
	sur = models.CharField(max_length=20)
	age = models.PositiveIntegerField()
class User(models.Model):
	log = models.CharField(max_length=20)
	pas = models.CharField(max_length=20)
	nam = models.CharField(max_length=20)
	sur = models.CharField(max_length=20)
	age = models.PositiveIntegerField()
class Cinema(models.Model):
	nam = models.CharField(max_length=20)
	add = models.CharField(max_length=50)
	pho = models.CharField(max_length=14)
class Hall(models.Model):
	sea = models.PositiveIntegerField()
	num = models.PositiveIntegerField()
	cin = models.ForeignKey(Cinema, on_delete = models.CASCADE)
class Movie(models.Model):
	nam = models.CharField(max_length=20)
	lim = models.CharField(max_length=5)
	dur = models.CharField(max_length=9)
class Schedule(models.Model):
	beg = models.CharField(max_length=22)
	end = models.CharField(max_length=22)
	pri = models.PositiveIntegerField()
	fil = models.ForeignKey(Movie, on_delete = models.CASCADE)
	hal = models.ForeignKey(Hall, on_delete = models.CASCADE)
class Ticket(models.Model):
	sch = models.ForeignKey(Schedule, on_delete = models.CASCADE)
	sea = models.PositiveIntegerField()
	ocu = models.BooleanField()
	hol = models.ForeignKey(User, on_delete = models.CASCADE)
class Movdes(models.Model):
	fil = models.ForeignKey(Movie, on_delete = models.CASCADE)
	path = models.CharField(max_length=22)
	desc = models.CharField(max_length=75)
	tag = models.CharField(max_length=40)