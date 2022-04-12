from django import forms
from django.forms import ModelForm
from .models import Eventtbl

#create event form
class EventForm(ModelForm):
	class Meta:
		model = Eventtbl
		fields = "__all__" # might not want all of the fields example:( 'event_id', 'event_email' ect)
		labels = {
			'event_id': '',
			'event_email': '',
			'date': '',
			'event_category': '',
			'event_description': '',
			'event_phone': '',
			'location_name': '',
		}

		widgets = {
			'event_id': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
			'event_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Contact Email'}),
			'date': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Event Date MM/DD/YYYY HH:MM'}),
			'event_category':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Type'}),
			'event_description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Descrition'}),
			'event_phone':  forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Contact Phone Number'}),
			'location_name':  forms.TextInput(attrs={'class':'form-control','placeholder': 'Location'}),
		}