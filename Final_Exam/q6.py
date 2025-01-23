def calculate_curr_age(birth_year,input_date):
	return birth_year-date.tm_year,date.tm_year
	
def leap_year_calculation(birth_year,curr_year,list_leapyear = []):
	if birth_year == curr_year:
		return list_leapyear
		
	if birth_year%4 == 0:
		if birth_year%400 == 0 and birth_year%100 == 0:
			list_leapyear.append(birth_year)
		elif birth_year%400 != 0 and birth_year%100 != 0:
			list_leapyear.append(birth_year)
				
	return leap_year_calculation(birth_year+1,curr_year)
	
import datetime
import time

now = datetime.datetime.now()
try:
	input_date = input("Enter your birthdate (YYYY-MM-DD): ")
	date = time.strptime(input_date,'%Y-%m-%d')
	if date.tm_year > now.year:
		print("The birth year higer than current year.")
	else:
		age,birth_year = calculate_curr_age(now.year,date)
		leap_years = leap_year_calculation(birth_year+1,now.year)
		print(f"Your current age is {age} years.")
		print("Leap years after your birthdate: ",leap_years)
except:
	print("Not valid input")
