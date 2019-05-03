from django import forms
from .models import User, Movie, Admin, Cinema, Hall, Schedule, Ticket
class Authform(forms.Form):
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password")
class Regform(forms.Form):
	log = forms.CharField(required = True, min_length=3, max_length=20, label="Enter Login")
	pas = forms.CharField(required = True, min_length=6, max_length=20, label="Enter Password")
	nam = forms.CharField(required = True, min_length=2, max_length=20, label="Enter Name")
	sur = forms.CharField(label="Enter Surname")
	age = forms.IntegerField(label="Enter Age", min_value=1)
class Movform(forms.Form):
	nam = forms.CharField(required = True, min_length=3, max_length=20, label="Enter movie name")
	lim = forms.CharField(required = True, min_length=3, max_length=5, label="Enter movie limit")
	dur = forms.CharField(required = True, max_length=9, label="Enter movie duration")
class Cinform(forms.Form):
	nam = forms.CharField(required = True, min_length=3, max_length=20, label="Enter cinema name")
	add = forms.CharField(required = True, max_length=50, label="Enter cinema address")
	pho = forms.CharField(required = True, max_length=14, label="Enter cinema phone number")
class Schform(forms.Form):
	beg = forms.CharField(required = True, min_length=8, max_length=22, label="Enter begin time of movie")
	end = forms.CharField(required = True, min_length=8, max_length=22, label="Enter end time of movie")
	pri = forms.IntegerField(required = True, min_value=1, label="Enter price of one ticket")
class Desform(forms.Form):
	tag = forms.CharField(required = True, min_length=3, label="Tag", widget=forms.Textarea)
	desc = forms.CharField(required = True, min_length=10, label="Description", widget=forms.Textarea)

