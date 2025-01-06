
##Logic
def options(dict1 = {}):
	print("Please Enter 1 for add option")
	print("Please Enter 2 for update option")
	print("Please Enter 3 for Delete option")
	print("Please Enter 4 for Display option")
	print("Please Enter 5 for Exit option")
	input_choice = eval(input("Enter Your Choice: "))
	
	
	if input_choice == 1:
	
		def add(dict1):
			country = []
			state = []
			city = []
			
			def add_country(dict1):
				input_country = input("Enter Country: ")
				if input_country.isalpha():
					country.append(input_country)
					res = input("Do You want to enter another Country Y/N: ")
					if res == "N" or res == 'n':
						dict1 = {k:{} for k in country}
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
				
				country_list = dict1.keys()
				print(list(country_list))
				country_choice = input("Which country you want to add the state please Enter: ")
				
				if country_choice in country_list:
					input_state = input("Enter State: ")
					if input_state.isalpha():
						state.append(input_state)
						res = input("Do You want to enter another State Y/N: ")
						if res == "N" or res == 'n':
							dict1 = dict1 | {country_choice:{k:[] for k in state}}
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
			print(dict1)
			
			permission = input("Do you enter the city Y/N: ")
			
			if permission == "Y" or permission == 'y':
				
				def add_city(dict1):
					try:
						country_list = dict1.keys()
						print(list(country_list))
						country_choice = input("Which country you want to add the city please Enter: ")
						state_list = dict1[country_choice].keys()
						print(list(state_list))
						state_choice = input("Which state you want to add city please Enter: ")
						if state_choice in state_list:
							input_city = input("Enter City: ")
							if input_city.isalpha():
								city.append(input_city)
								res = input("Do You want to enter another City Y/N: ")
								if res == "N" or res == 'n':
									dict1 = dict1 | {country_choice:dict1[country_choice] | 			{state_choice:[v for v in city]}}
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
				
			return dict1
			
		dict1 = add(dict1)
	
		options(dict1)	
				
	elif input_choice == 2:
		
		def update(dict1):
		
			permission_update = input("which option you want to change country, state and city: ")
			
			if permission_update == "country":
				def update_country():
					country_list = dict1.keys()
					print(list(country_list))
					country_choice = input("Which country you want to Update please Enter: ")
					if country_choice in country_list:
						dict1.pop(country_choice)
						update_country_name = input("Please Enter country new name: ")
						dict1[update_country_name] = {}
					else:
						print("You are selected country is not in list")
						update_country()
				
				update_country()
						
			elif permission_update == "state":	
				def update_state():
					try:
						country_list = dict1.keys()
						print(list(country_list))
						country_choice = input("Which country you want to Update please Enter: ")
						state_list = dict1[country_choice].keys()
						print(list(state_list))
						state_choice = input("Which state you want to Update please Enter: ")
						if state_choice in state_list:
							dict1[country_choice].pop(state_choice)
							update_state_name = input("Please Enter state new name: ")
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
						country_list = dict1.keys()
						print(list(country_list))
						country_choice = input("Which country you want to Update please Enter: ")
						state_list = dict1[country_choice].keys()
						print(list(state_list))
						state_choice = input("Which state you want to Update please Enter: ")	
						city_list = dict1[country_choice][state_choice]
						print(list(city_list))
						city_choice = input("Which city you want to Update please Enter: ")
						if city_choice in city_list:
							dict1[country_choice][state_choice].remove(city_choice)
							update_city_name = input("Please Enter new city: ")
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
					country_list = dict1.keys()
					print(list(country_list))
					country_choice = input("Which country you want to Delete please Enter: ")
					if country_choice in country_list:
						del dict1[country_choice]
					else:
						print("You are selected country is not in list")
						delete_country()
				
				delete_country()
				
			elif permission_delete == "state":
				def delete_state():
					try:
						country_list = dict1.keys()
						print(list(country_list))
						country_choice = input("Which country you want to Delete please Enter: ")
						state_list = dict1[country_choice].keys()
						print(list(state_list))
						state_choice = input("Which state you want to Delete please Enter: ")
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
	
						country_list = dict1.keys()
						print(list(country_list))
						country_choice = input("Which country you want to Delete please Enter: ")
						state_list = dict1[country_choice].keys()
						print(list(state_list))
						state_choice = input("Which state you want to Delete please Enter: ")	
						city_list = dict1[country_choice][state_choice]
						print(list(city_list))
						city_choice = input("Which city you want to Delete please Enter: ")
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
	
options()
