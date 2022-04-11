from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Usertbl
from .models import Eventtbl

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