from django import forms
from django.forms import ModelForm
from .models import Eventtbl, University, Rso, Review

#create event form
class EventForm(ModelForm):
	class Meta:
		model = Eventtbl
		fields = "__all__" # might not want all of the fields example:( 'event_id', 'event_email' ect)

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
