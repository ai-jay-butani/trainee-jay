
##Logic
def options(dict1 = {}):
	print("Please Enter 1 for add option")
	print("Please Enter 2 for update option")
	print("Please Enter 3 for Delete option")
	print("Please Enter 4 for Display option")
	print("Please Enter 5 for Exit option")
	input_choice = eval(input("Enter Your Choice: "))
	
	def general_list(data,_name,option,add_name=''):
		gen_list = list(data.keys())
		print(gen_list)
		choice = input(f"Which {_name} you want to {option} the {add_name} please Enter: ")
		choice = choice.lower()
		return choice,gen_list
	
	if input_choice == 1:
	
		def add(dict1):
			country = []
	
			def add_country(dict1):
				input_country = input("Enter Country: ")
				input_country = input_country.lower()
				if input_country.isalpha():
					country.append(input_country)
					res = input("Do You want to enter another Country Y/N: ")
					if res == "N" or res == 'n':
						dict1 = dict1 | {k:{} for k in country}
						return dict1
					else:
						dict1 = add_country(dict1)
						return dict1
				else:
					print("Country name is not valid")
					dict1 = add_country(dict1)
					return dict1
					
					
			dict1 = add_country(dict1)
	
			def add_state(dict1):
				
				country_choice,country_list = general_list(dict1,"country","add","state")
				if country_choice in country_list:
					input_state = input("Enter State: ")
					input_state = input_state.lower()
					if input_state.isalpha():
						dict1[country_choice][input_state] = []
						res = input("Do You want to enter another State Y/N: ")
						if res == "N" or res == 'n':
							return dict1
						else:
							return add_state(dict1)
					else:
						print("State name is not valid")
						return add_state(dict1)
				else:
					print("You are selected country is not in list")
					return add_state(dict1)
					
				
					
			dict1 = add_state(dict1)
			
			permission = input("Do you enter the city Y/N: ")
			
			if permission == "Y" or permission == 'y':
				
				def add_city(dict1):
					try:
						country_choice,country_list = general_list(dict1,"country","add","city")
						state_choice,state_list = general_list(dict1[country_choice],"state","add","city")
						if state_choice in state_list:
							input_city = input("Enter City: ")
							input_city = input_city.lower()
							if input_city.isalpha():
								dict1[country_choice][state_choice].append(input_city)
								res = input("Do You want to enter another City Y/N: ")
								if res == "N" or res == 'n':
									return dict1
								else:
									return add_city(dict1)
							else:
								print("city name is not valid")
								return add_city(dict1)
						
						else:
							print("You are selected state is not in list")
							return add_city(dict1)
					except:
						print("country is not found in list.")
						return add_city(dict1)
								
				dict1 = add_city(dict1)	
			else:
				options(dict1)
				
			return dict1
			
		dict1 = add(dict1)
	
		options(dict1)	
				
	elif input_choice == 2:
		
		def update(dict1):
		
			permission_update = input("which option you want to change country, state and city: ")
			
			if permission_update == "country":
				def update_country():
					country_choice,country_list = general_list(dict1,"country","update")
					if country_choice in country_list:
						dict1.pop(country_choice)
						update_country_name = input("Please Enter country new name: ")
						update_country_name  = update_country_name.lower()
						dict1[update_country_name] = {}
					else:
						print("You are selected country is not in list")
						update_country()
				
				update_country()
						
			elif permission_update == "state":	
				def update_state():
					try:
						country_choice,country_list = general_list(dict1,"country","update")
						state_choice, state_list = general_list(dict1[country_choice],"state","update")
						if state_choice in state_list:
							dict1[country_choice].pop(state_choice)
							update_state_name = input("Please Enter state new name: ")
							update_state_name  = update_state_name.lower()
							dict1[country_choice][update_state_name] = []
						else:
							print("You are selected state is not in list")
							update_state()
					except:
						print("country is not found in list.")
						update_state()
					
				update_state()
					
			elif permission_update == "city":	
				def update_city():
					try:
						country_choice,country_list = general_list(dict1,"country","update")
						state_choice, state_list = general_list(dict1[country_choice],"state","update")
						city_list = dict1[country_choice][state_choice]
						print(list(city_list))
						city_choice = input("Which city you want to Update please Enter: ")
						city_choice = city_choice.lower()
						if city_choice in city_list:
							dict1[country_choice][state_choice].remove(city_choice)
							update_city_name = input("Please Enter new city: ")
							update_city_name  = update_city_name.lower()
							dict1[country_choice][state_choice].append(update_city_name)
						else:
							print("You are selected city is not in list")
							update_city()
					except:
						print("country or state is not found in list.")
						update_city()	
							
				update_city()
					
			else:
				print("You are not selected valid permission")
				update(dict1)	
			
			return dict1
		dict1 = update(dict1)
		
		options(dict1)
		
	elif input_choice == 3:
		
		def delete(dict1):
		
			permission_delete = input("which option you want to delete country, state and city: ")
			
			if permission_delete == "country":
				def delete_country():
					country_choice,country_list = general_list(dict1,"country","delete")
					if country_choice in country_list:
						del dict1[country_choice]
					else:
						print("You are selected country is not in list")
						delete_country()
				
				delete_country()
				
			elif permission_delete == "state":
				def delete_state():
					try:
						country_choice, country_list = general_list(dict1,"country","delete")
						state_choice,state_list = general_list(dict1[country_choice],"state","delete")
						if state_choice in state_list:
							del dict1[country_choice][state_choice]
						else:
							print("You are selected state is not in list")
							delete_state()
							
					except:
						print("country is not found in list.")
						delete_state()
						
					
				delete_state()
					
			elif permission_delete == "city":
				def delete_city():
					try:
	
						country_choice, country_list = general_list(dict1,"country","delete")
						state_choice, state_list = general_list(dict1[country_choice],"state","delete")
						city_list = dict1[country_choice][state_choice]
						print(list(city_list))
						city_choice = input("Which city you want to Delete please Enter: ")
						city_choice = city_choice.lower()
						if city_choice in city_list:
							city_list.remove(city_choice)
						else:
							print("You are selected city is not in list")
							delete_city()
										
					except:
						print("country or state is not found in list.")	
						delete_city()
							
				delete_city()
					
			else:
				print("You are not selected valid permission")	
				delete(dict1)
				
			return dict1
			
		dict1 = delete(dict1)
		
		options(dict1)
			
	elif input_choice == 4:
		
		print(dict1)
		options(dict1)
	
	elif input_choice == 5:
	
		return
		
	else:
	
		print("Not Selected Valid Option")
		options()
	
	
	
	
##main	
	
import time

start_time = time.time()
print(start_time)	
options()
end_time = time.time()
print(end_time)

print("Time taken by function: ",end_time-start_time)
