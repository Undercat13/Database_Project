from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Usertbl
from .models import Eventtbl
from .forms import EventForm, UniversityForm, RsoForm, ReviewForm
from django.http import HttpResponseRedirect

def all_events(request):
	event_lsit = Eventtbl.objects.all()

# Create your views here.
def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
	name = "John"
	month = month.capitalize()
	# convert month name -> num
	month_num = list(calendar.month_name).index(month)
	month_num = int(month_num)

	#create a calendar
	cal = HTMLCalendar().formatmonth(year, month_num)
	now = datetime.now()
	current_year = now.year

	users = Usertbl.objects.all()

	time = now.strftime('%I:%M:%S %p')
	return render(request, 'events/home.html', {
		"first_name": name,
		"year": year,
		"month": month,
		"month_num": month_num,
		"cal": cal,
		"current_year": current_year,
		"time": time,
		"users": users
		})

def add_event(request):
	submitted = False
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_event?submitted=True')
	else:
		form = EventForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'events/add_event.html',
		{
		'form': form,
		'submitted': submitted
		})

def add_university(request):
	submitted = False
	if request.method == "POST":
		form = UniversityForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_university?submitted=True')
	else:
		form = UniversityForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'events/add_university.html',
		{
		'form': form,
		'submitted': submitted
		})

def add_rso(request):
	submitted = False
	if request.method == "POST":
		form = RsoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_rso?submitted=True')
	else:
		form = RsoForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'events/add_rso.html',
		{
		'form': form,
		'submitted': submitted
		})

def add_review(request):
	submitted = False
	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_review?submitted=True')
	else:
		form = ReviewForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'events/add_review.html',
		{
		'form': form,
		'submitted': submitted
		})
