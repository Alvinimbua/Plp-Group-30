# Day 1 Task 1
# Bus Fare Challenge

from datetime import date

date = date.today()

day = date.strftime('%A')
short_form_day = day[:3]

print('Date: ',date)

print('Day: ',short_form_day)

if day == 'Saturday':
    print('Fare: 60')

elif day == 'Sunday':
    print('Fare: 80')

else:
    print('Fare: 100')