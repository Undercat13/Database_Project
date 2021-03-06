from django.shortcuts import render, redirect
import calendar
import random
from calendar import HTMLCalendar
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from events.models import Usertbl
from .models import Eventtbl, Rso, University, Review, Events_usertbl, location
from .forms import EventForm, RegistrationForm, UniversityForm, RsoForm, ReviewForm,LocationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


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

	users = Events_usertbl.objects.all()

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
		form2 = LocationForm(request.POST)
		if form.is_valid() and form2.is_valid():
			form.instance.admin_id = request.user.user_id
			form.instance.uni_id = request.user.uni_id
			if (form.instance.rso_host != 0):
				rso = Rso.objects.get(rso_id = form.instance.rso_host)
				rso.num_events += 1
				rso.save()
			form.instance.location_name = form2.instance.location_name
			form.save()
			form2.save()
			return HttpResponseRedirect('/add_event?submitted=True')
	else:
		form = EventForm(initial={"rso_host": "0"})
		form2 = LocationForm()
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'events/add_event.html',
		{
		'form': form,
		'form2': form2,
		'submitted': submitted
		})

def add_university(request):
	submitted = False
	curr_user = request.user
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
		'submitted': submitted,
		'curr_user': curr_user
		})

def add_rso(request):
	submitted = False
	if request.method == "POST":
		form = RsoForm(request.POST)
		if form.is_valid():
			form.instance.admin_id = request.user.user_id
			form.instance.uni_id = request.user.uni_id
			#add rso_id to rso_ids on user
			request.user.rso_ids = request.user.rso_ids	+ ',' + str(form.instance.rso_id)
			form.instance.num_students += 1
			form.save()
			request.user.save()
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

def add_review(request, curr_event):
	submitted = False
	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.instance.event_id = curr_event
			form.instance.user_id = request.user.user_id
			form.save()
			return HttpResponseRedirect('/view_event/{}'.format(curr_event))
	else:
		form = ReviewForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'events/add_review.html',{'form': form,
		'submitted': submitted,})

def rso_list(request):
	rsos = Rso.objects.all()
	curr_user = request.user
	if (type(curr_user.rso_ids) == 'NoneType'):
		curr_user_rsos = curr_user.rso_ids.split(",")
		for i in range(0, len(curr_user_rsos)):
			curr_user_rsos[i] = int(curr_user_rsos[i])
	else:
		curr_user_rsos = ""

	curr_user_rsos_list = Rso.objects.filter(rso_id__in = curr_user_rsos)
	return render(request, 'events/list_rso.html', {'rsos':rsos, 'curr_user_rsos_list':curr_user_rsos_list, 'curr_user': curr_user})

def view_rso(request, curr_rso):
	joined = False
	user = request.user
	rso = Rso.objects.get(pk = curr_rso)
	if request.method == "POST":
		#add rso_id to rso_ids on user
		user.rso_ids = user.rso_ids	+ ',' + str(rso.rso_id)
		rso.num_students += 1
		if( rso.num_students == 4):
			rso.is_valid = True
			rso.admin_id = user.user_id
			user.user_type = "Admin"
		rso.save()
		request.user.save()
		messages.success(request, "Added to RSO")
	return render(request, 'events/view_rso.html', {'rso':rso, 'user':user})

def events_list(request):
	events = Eventtbl.objects.all()
	curr_user = request.user
	return render(request, 'events/list_events.html', {'events':events,'curr_user':curr_user})

def view_event(request, curr_event):
	event = Eventtbl.objects.get(pk = curr_event)
	curr_user = request.user
	users = Events_usertbl.objects.all()
	reviews = Review.objects.filter(event_id = curr_event)
	local  = location.objects.get(pk = event.location_name)
	local.latitude = float(local.latitude)
	local.longitude = float(local.longitude)
	return render(request, 'events/view_event.html', {'event':event, 'reviews':reviews, 'users': users, 'curr_user':curr_user, 'local':local})

def universities_list(request):
	universities = University.objects.all()
	user = request.user
	return render(request, 'events/list_universities.html', {'universities':universities, 'user': user})

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
			return redirect('events_list')
			# Redirect to a success page.
		else:
			messages.success(request, "There was an error logging in try again.")
			return redirect('login_user')
	else:
		return render(request, 'events/login_user.html', {})

def edit_rso(request, curr_rso):
	submitted = False
	rso = Rso.objects.get(pk = curr_rso)
	if request.method == "POST":
		form = RsoForm(request.POST, instance = rso)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/rso_list')
	else:
		form = RsoForm(instance = rso)
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/edit_rso.html', {'rso':rso, 'form': form,
		'submitted': submitted})

def edit_event(request, curr_event):
	submitted = False
	event = Eventtbl.objects.get(pk = curr_event)
	if request.method == "POST":
		form = EventForm(request.POST, instance = event)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/events_list')
	else:
		form = EventForm(instance = event)
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/edit_rso.html', {'event':event, 'form': form,
		'submitted': submitted})


def edit_university(request, curr_university):
	submitted = False
	university = University.objects.get(pk = curr_university)
	if request.method == "POST":
		form = UniversityForm(request.POST, instance = university)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/universities_list')
	else:
		form = UniversityForm(instance = university)
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/edit_university.html', {'university':university, 'form': form,
		'submitted': submitted})

def edit_review(request, curr_event, curr_user):
	submitted = False
	review = Review.objects.filter(user_id = curr_user, event_id=curr_event).first()
	if request.method == "POST":
		form = ReviewForm(request.POST, instance = review)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/view_event/{}'.format(curr_event))
	else:
		form = ReviewForm(instance = review)
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'events/edit_review.html',{'review':review, 'form': form,
		'submitted': submitted})

def logout_user(request):
	logout(request)
	messages.success(request, ("You were successfully logged out"))
	return redirect('events_list')

def register_user(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			user.user_type = "Student"
			login(request, user)
			messages.success(request, ("registration Successful"))
			uni = University.objects.get(uni_id = form.instance.uni_id)
			uni.num_students += 1
			uni.save()
			return redirect('events_list')
	else:
		form = RegistrationForm()

	return render(request, 'events/register_user.html', {
		'form': form
		})