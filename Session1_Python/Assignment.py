##Logic
def options(main_data = {}):
	print("Please Enter 1 for add option")
	print("Please Enter 2 for update option")
	print("Please Enter 3 for Delete option")
	print("Please Enter 4 for Display option")
	print("Please Enter 5 for Exit option")
	input_choice = eval(input("Enter Your Choice: "))
	
	def general_list(data,_name,option,add_name=''):
		gen_list = list(data.keys())
		if gen_list == []:
			return '',gen_list
		else:
			print(gen_list)
			choice = input(f"Which {_name} you want to {option} the {add_name} please Enter: ")
			choice = choice.lower()
			return choice,gen_list
		
	def check_duplicate(data,city):
		if city in data:
			return False
		else:
			return True
	
	if input_choice == 1:
	
		def add():
	
			def add_country():
				input_country = input("Enter Country: ")
				input_country = input_country.lower()
				if input_country.isalpha():
					main_data[input_country] = {}
					res = input("Do You want to enter another Country Y/N: ")
					if res == "N" or res == 'n':
						pass
					else:
						add_country()
				else:
					print("Country name is not valid")
					add_country()
					
			add_country()
			
			def add_state():
			
				country_choice,country_list = general_list(main_data, "country", "add", "state")
				if country_choice in country_list:
					input_state = input("Enter State: ")
					input_state = input_state.lower()
					if input_state.isalpha():
						main_data[country_choice][input_state] = []
						res = input("Do You want to enter another State Y/N: ")
						if res == "N" or res == 'n':
							pass
						else:
							add_state()
					else:
						print("State name is not valid")
						add_state()
				else:
					print("You are selected country is not in list")
					add_state()
					
			add_state()
			
			permission = input("Do you enter the city Y/N: ")
			
			if permission == "Y" or permission == 'y':
				
				def add_city():
					try:
						country_choice,country_list = general_list(main_data, "country", "add", "city")
						state_choice,state_list = general_list(main_data[country_choice], "state", "add", "city")
						if state_choice in state_list:
							input_city = input("Enter City: ")
							input_city = input_city.lower()
							if input_city.isalpha():
								if check_duplicate(main_data[country_choice][state_choice], input_city):
									main_data[country_choice][state_choice].append(input_city)
								else:
									print("This city is already in data.")
								res = input("Do You want to enter another City Y/N: ")
								if res == "N" or res == 'n':
									pass
								else:
									add_city()
							else:
								print("city name is not valid")
								add_city()
						
						else:
							print("You are selected state is not in list")
							add_city()
					except:
						print("country is not found in list.")
						add_city()
								
				add_city()	
		add()
		options(main_data)
				
	elif input_choice == 2:
		
		def update():
		
			permission_update = input("which option you want to change country, state and city: ")
			
			if permission_update == "country":
				def update_country():
					country_choice,country_list = general_list(main_data, "country", "update")
					if country_choice in country_list:
						main_data.pop(country_choice)
						update_country_name = input("Please Enter country new name: ")
						update_country_name  = update_country_name.lower()
						main_data[update_country_name] = {}
					else:
						print("You are selected country is not in list")
						update_country()
				
				update_country()
						
			elif permission_update == "state":	
				def update_state():
					try:
						country_choice,country_list = general_list(main_data, "country", "update")
						state_choice, state_list = general_list(main_data[country_choice], "state", "update")
						if state_list == []:
							print("Not any state in list")
						elif state_choice in state_list:
							main_data[country_choice].pop(state_choice)
							update_state_name = input("Please Enter state new name: ")
							update_state_name  = update_state_name.lower()
							main_data[country_choice][update_state_name] = []
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
						country_choice,country_list = general_list(main_data, "country", "update")
						state_choice, state_list = general_list(main_data[country_choice], "state", "update")
						city_list = main_data[country_choice][state_choice]
						print(list(city_list))
						city_choice = input("Which city you want to Update please Enter: ")
						city_choice = city_choice.lower()
						if city_choice in city_list:
							update_city_name = input("Please Enter new city: ")
							update_city_name  = update_city_name.lower()
							if check_duplicate(main_data[country_choice][state_choice], update_city_name):
								main_data[country_choice][state_choice].remove(city_choice)
								main_data[country_choice][state_choice].append(update_city_name)
							else:
								print("The city is already in data.")
								update_city()
						else:
							print("You are selected city is not in list")
							update_city()
					except:
						print("country or state is not found in list.")
						update_city()	
							
				update_city()
					
			else:
				print("You are not selected valid permission")
				update()	
		
		update()
		options(main_data)
		
	elif input_choice == 3:
		
		def delete():
		
			permission_delete = input("which option you want to delete country, state and city: ")
			
			if permission_delete == "country":
				def delete_country():
					country_choice,country_list = general_list(main_data, "country", "delete")
					if country_choice in country_list:
						del main_data[country_choice]
					else:
						print("You are selected country is not in list")
						delete_country()
				
				delete_country()
				
			elif permission_delete == "state":
				def delete_state():
					try:
						country_choice, country_list = general_list(main_data, "country", "delete")
						state_choice,state_list = general_list(main_data[country_choice], "state", "delete")
						if state_choice in state_list:
							del main_data[country_choice][state_choice]
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
						country_choice, country_list = general_list(main_data, "country", "delete")
						state_choice, state_list = general_list(main_data[country_choice], "state", "delete")
						city_list = main_data[country_choice][state_choice]
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
				delete()
		delete()
		options(main_data)
			
	elif input_choice == 4:
		print(main_data)
		options(main_data)
	
	elif input_choice == 5:
		return
		
	else:
	
		print("Not Selected Valid Option")
		options()

##main	
import time
start_time = time.time()	
options()
end_time = time.time()
print("Time taken by function: ",end_time-start_time)
