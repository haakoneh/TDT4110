def is_leap_year (year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	return False

def weekday_newyear(day, day_list):
	return day_list[day]

def is_workday(weekday):
	if(weekday == 5 or weekday == 6):
		return False
	else: return True

# def workdays_in_year(year, firstday):
	# if(is_leap_year (year)):
		
	
	# else:
		# for i in range (0, 365):
			
	

def main():
	day = 0
	day_list = ['man', 'tir', 'ons', 'tor', 'fre', 'lor', 'son']
	
	for i in range(1900, 1920):
		weekday = weekday_newyear(day, day_list)
		print(i, weekday)
		if(is_leap_year(i)):
			day += 2
		else: day += 1
		day = day % 7

main()