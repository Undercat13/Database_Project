from django import forms
from django.forms import ModelForm
from .models import Eventtbl, University, Rso, Review

#create event form
class EventForm(ModelForm):
	class Meta:
		model = Eventtbl
		fields = "__all__" # might not want all of the fields example:( 'event_id', 'event_email' ect)
		labels = {
			'event_id': 'Event ID Number:',
			'event_email': 'Contact Email:',
			'date': 'Event Date:',
			'event_category': 'Choose the type of event:',
			'event_description': 'Event Descrition:',
			'event_phone': 'Contact Phone Number:',
			'location_name': 'Event Location:',
		}
		CATEGORY = [
			('public', 'Public'),
			('private', 'Private'),
			('rso', 'Rso')
		]
		widgets = {
			'event_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': '#'}),
			'event_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'contact@email.com'}),
			'date': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'MM/DD/YYYY HH:MM'}),
			'event_category':  forms.Select(choices=CATEGORY, attrs={'class':'form-control'}),
			'event_description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descrition'}),
			'event_phone':  forms.NumberInput(attrs={'class':'form-control', 'placeholder': '### ### ####'}),
			'location_name':  forms.TextInput(attrs={'class':'form-control','placeholder': 'Location'}),
		}

class UniversityForm(ModelForm):
	class Meta:
		model = University
		fields = ['uni_id', 'uni_name', 'num_students', 'uni_description', 'uni_location'] # does not include addition of gallery photos for now.

class RsoForm(ModelForm):
	class Meta:
		model = Rso
		fields = "__all__"

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = "__all__"

