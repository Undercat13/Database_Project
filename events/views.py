from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .models import Usertbl, Eventtbl, Rso, University
from .forms import EventForm, UniversityForm, RsoForm, ReviewForm
from django.http import HttpResponseRedirect
from django.contrib import messages

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

def rso_list(request):
	rsos = Rso.objects.all()
	return render(request, 'events/list_rso.html', {'rsos':rsos})

def view_rso(request, curr_rso):
	rso = Rso.objects.get(pk = curr_rso)
	return render(request, 'events/view_rso.html', {'rso':rso})

def events_list(request):
	events = Eventtbl.objects.all()
	return render(request, 'events/list_events.html', {'events':events})

def view_event(request, curr_event):
	event = Eventtbl.objects.get(pk = curr_event)
	return render(request, 'events/view_event.html', {'event':event})

def universities_list(request):
	universities = University.objects.all()
	return render(request, 'events/list_universities.html', {'universities':universities})

def view_university(request, curr_uni):
	university = University.objects.get(pk = curr_uni)
	return render(request, 'events/view_university.html', {'university':university})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
			# Redirect to a success page.
		else:
			messages.success(request, "There was an error logging in try again.")
			return redirect('login_user')
	else:
		return render(request, 'events/login_user.html', {})