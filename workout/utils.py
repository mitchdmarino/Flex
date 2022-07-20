# https://www.huiwenteo.com/normal/2018/07/29/django-calendar-ii.html
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Workout

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter workouts by day
	def formatday(self, day, workouts, user):
		workouts_per_day = workouts.filter(day__day=day, user_id=user.id)
		d = ''
		for workout in workouts_per_day:
			color = 'black'
			if workout.complete:
				color = 'green'
			d += f'<li style="color:{color}"> {workout.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, workouts, user):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, workouts, user)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter workouts by year and month
	def formatmonth(self, user, withyear=True):
		workouts = Workout.objects.filter(day__year=self.year, day__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, workouts, user)}\n'
		return cal
