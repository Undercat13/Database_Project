from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usertbl, Eventtbl, University, Rso, Review

#create event form
class EventForm(ModelForm):
	class Meta:
		model = Eventtbl
		fields = "__all__" # might not want all of the fields example:( 'event_id', 'event_email' ect)
		labels = {
			'name': 'Event Name:',
			'event_id': 'Event ID Number:',
			'event_email': 'Contact Email:',
			'date': 'Event Date:',
			'event_category': 'Choose the type of event:',
			'event_description': 'Event Description:',
			'event_phone': 'Contact Phone Number:',
			'location_name': 'Event Location:',
			'event_type': 'Event Type:',
			'rso_host': 'Host Rso:',
			'admin_id': 'admin_id:'
		}
		CATEGORY = [
			('public', 'Public'),
			('private', 'Private'),
			('rso', 'Rso')
		]
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
			'event_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'event_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'contact@email.com'}),
			'date': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'MM/DD/YYYY HH:MM'}),
			'event_category':  forms.Select(choices=CATEGORY, attrs={'class':'form-control'}),
			'event_description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Description'}),
			'event_phone':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '### ### ####'}),
			'location_name':  forms.TextInput(attrs={'class':'form-control','placeholder': 'Location'}),
			'event_type':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Type of Event'}),
			'rso_host':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Host Rso'}),
			'admin_id':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
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
		fields = ['rso_id', 'uni_id', 'num_students', 'num_events']
		labels = {
			'rso_id': 'Rso ID Number:',
			'uni_id': 'Corresponding University Id:',
			'num_students': 'Number of Students:',
			'num_events': 'Number of Events:',
		}
		widgets = {
			'rso_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'uni_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'num_students':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'num_events':  forms.NumberInput(attrs={'class':'form-control','placeholder': '#'})
		}

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = [ 'comment', 'rating']
		labels = {
			'rating': 'Your Rating (out of 10):',
			'comment': 'Enter Your Review:',
			#'user_id': 'Enter your User Id:',
		}
		widgets = {
			'rating': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Comment Here'}),
			#'user_id':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
		}

class RegistrationForm(UserCreationForm):
	"""docstring for RegistrationForm"""
	user_id = forms.IntegerField()
	uni_id = forms.IntegerField()
	username = forms.CharField(max_length=150)
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)
	

	class Meta: # define a metadata related to this class
		model = Usertbl
		fields = (
			'user_id',
			'uni_id',
			'username',
			'password1',
			'password2',

		)
	# def save(self, commit=True):
	# 	user = super(RegistrationForm, self).save(commit=False)
