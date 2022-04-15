from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usertbl, Eventtbl, University, Rso, Review

#create event form
class EventForm(ModelForm):
	class Meta:
		model = Eventtbl
		fields = ['name', 'event_id', 'event_email', 'date', 'event_category', 'event_description', 'event_phone', 'location_name', 'event_type', 'rso_host'] # might not want all of the fields example:( 'event_id', 'event_email' ect)
		labels = {
			'name': 'Event Name:',
			'event_id': 'Event ID Number:',
			'event_email': 'Contact Email:',
			'date': 'Event Date:',
			'event_category': 'Choose the category of event:',
			'event_description': 'Event Description:',
			'event_phone': 'Contact Phone Number:',
			'location_name': 'Event Location:',
			'event_type': 'Event Type:',
			'rso_host': 'Host Rso:',
		}
		types = [
			('public', 'Public'),
			('private', 'Private'),
			('rso', 'Rso')
		]
		categories = [
			('sports', 'Sports'),
			('tech talk', 'Tech Talk'),
			('social', 'Social'),
			('concert','Concert'),
			('lecture', 'lecture'),
			('fundraising', 'Fundraising'),
			('competition', 'Competition')
		]

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
			'event_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'event_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'contact@email.com'}),
			'date': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'MM/DD/YYYY HH:MM'}),
			'event_category':  forms.Select(choices=types, attrs={'class':'form-control'}),
			'event_description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Description'}),
			'event_phone':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '### ### ####'}),
			'location_name':  forms.TextInput(attrs={'class':'form-control','placeholder': 'Location'}),
			'event_type':  forms.Select(choices=categories, attrs={'class':'form-control'}),
			'rso_host':  forms.NumberInput(attrs={'class':'form-control', 'initial': "0"}),
		}

class UniversityForm(ModelForm):
	class Meta:
		model = University
		fields = ['uni_id', 'uni_name', 'num_students', 'uni_description', 'uni_location']
		labels = {
			'uni_id': 'University ID Number:',
			'uni_name': 'University Name:',
			'num_students': 'Number of Students:',
			'uni_description': 'Description for University:',
			'uni_location': 'Location for University:',
		}
		widgets = {
			'uni_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'uni_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
			'num_students':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'uni_description':  forms.TextInput(attrs={'class':'form-control','placeholder': 'Description'}),
			'uni_location':  forms.TextInput(attrs={'class':'form-control','placeholder': 'Location'}),
		}

class RsoForm(ModelForm):
	class Meta:
		model = Rso
		fields = ['name','rso_id', 'num_students', 'num_events']
		labels = {
			'name': 'Rso Name:',
			'rso_id': 'Rso ID Number:',
			'num_students': 'Number of Students:',
			'num_events': 'Number of Events:',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'rso_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			#'uni_id': forms.Select(attrs={'class':'form-control', 'placeholder': '#'}),
			'num_students':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'num_events':  forms.NumberInput(attrs={'class':'form-control','placeholder': '#'})
		}

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = [ 'comment', 'rating']
		labels = {
			'rating': 'Your Rating (out of 5):',
			'comment': 'Enter Your Review:',
			#'user_id': 'Enter your User Id:',
		}
		widgets = {
			'rating': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Comment Here'}),
			#'user_id':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
		}

class RegistrationForm(UserCreationForm):
	class Meta: # define a metadata related to this class
		model = Usertbl
		fields = (
			'username',
			'password1',
			'password2',
			'user_id',
			'uni_id',

		)
		widgets = {
			'username': forms.TextInput(),
			'password1': forms.PasswordInput(),
			'password2': forms.PasswordInput(),
			'user_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'uni_id': forms.Select(choices=[(uni.uni_id, uni.uni_name) for uni in University.objects.all()], attrs={'class':'form-control'}),
			}
