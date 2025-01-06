
##Logic
def options(dict1 = {}):
	print("Please Enter 1 for add option")
	print("Please Enter 2 for update option")
	print("Please Enter 3 for Delete option")
	print("Please Enter 4 for Exit option")
	input_choice = eval(input("Enter Your Choice: "))
	
	
	if input_choice == 1:
	
		def add():
		
			
			def add_country():
				input_country = input("Enter Country: ")
				dict1[input_country] = {}
				res = input("Do You want to enter another Country Y/N: ")
				if res == "N" or res == 'n':
					pass
				else:
					add_country()
					
			add_country()
			
			country_list = dict1.keys()
			print(country_list)
			country_choice = input("Which country you want to add the state please Enter: ")
			
			def add_state():
				
				if country_choice in country_list:
					input_state = input("Enter State: ")
					dict1[country_choice][input_state] = []
					res = input("Do You want to enter another State Y/N: ")
					if res == "N":
						pass
					else:
						add_state()
				else:
					print("You are selected country is not in list")
					
			add_state()
			
			permission = input("Do you enter the city Y/N: ")
			
			if permission == "Y":
				try:
					country_list = dict1.keys()
					print(country_list)
					country_choice = input("Which country you want to add the city please Enter: ")
					state_list = dict1[country_choice].keys()
					print(state_list)
					state_choice = input("Which state you want to add city please Enter: ")
					
					def add_city():
						if state_choice in state_list:
							input_city = input("Enter City: ")
							dict1[country_choice][state_choice].append(input_city)
							res = input("Do You want to enter another City Y/N: ")
							if res == "N":
								pass
							else:
								add_city()
						else:
							print("You are selected state is not in list")
								
					add_city()
						
				except:
					print("country is not found in list.")
			
				
		add()
	
		options(dict1)	
				
	elif input_choice == 2:
		
		def update():
		
			permission_update = input("which option you want to change country, state and city: ")
			
			if permission_update == "country":
				country_list = dict1.keys()
				print(country_list)
				country_choice = input("Which country you want to Update please Enter: ")
				
				def update_country():
					if country_choice in country_list:
						dict1.pop(country_choice)
						update_country_name = input("Please Enter country new name: ")
						dict1[update_country_name] = {}
					else:
						print("You are selected country is not in list")
				
				update_country()
						
			elif permission_update == "state":
				try:
					country_list = dict1.keys()
					print(country_list)
					country_choice = input("Which country you want to Update please Enter: ")
					state_list = dict1[country_choice].keys()
					print(state_list)
					state_choice = input("Which state you want to Update please Enter: ")
					
					def update_state():
						if state_choice in state_list:
							dict1[country_choice].pop(state_choice)
							update_state_name = input("Please Enter state new name: ")
							dict1[country_choice][update_state_name] = []
						else:
							print("You are selected state is not in list")
					
					update_state()
					 
				except:
					print("country is not found in list.")
					
			elif permission_update == "city":
				try:
				
					country_list = dict1.keys()
					print(country_list)
					country_choice = input("Which country you want to Update please Enter: ")
					state_list = dict1[country_choice].keys()
					print(state_list)
					state_choice = input("Which state you want to Update please Enter: ")	
					city_list = dict1[country_choice][state_choice]
					print(city_list)
					city_choice = input("Which city you want to Update please Enter: ")
					
					def update_city():
						if city_choice in city_list:
							dict1[country_choice][state_choice].remove(city_choice)
							update_city_name = input("Please Enter new city: ")
							dict1[country_choice][state_choice].append(update_city_name)
						else:
							print("You are selected city is not in list")
							
					update_city()
					
				except:
					print("country or state is not found in list.")	
					
			else:
				print("You are not selected valid permission")	
		
		update()
		
		options(dict1)
		
	elif input_choice == 3:
		
		def delete():
		
			permission_delete = input("which option you want to delete country, state and city: ")
			
			if permission_delete == "country":
				country_list = dict1.keys()
				print(country_list)
				country_choice = input("Which country you want to Delete please Enter: ")
				
				def delete_country():
					if country_choice in country_list:
						del dict1[country_choice]
					else:
						print("You are selected country is not in list")
				
				delete_country()
				
			elif permission_delete == "state":
				try:
					country_list = dict1.keys()
					print(country_list)
					country_choice = input("Which country you want to Delete please Enter: ")
					state_list = dict1[country_choice].keys()
					print(state_list)
					state_choice = input("Which state you want to Delete please Enter: ")
					
					def delete_state():
						if state_choice in state_list:
							del dict1[country_choice][state_choice]
						else:
							print("You are selected state is not in list")
					
					delete_state()
					 
				except:
					print("country is not found in list.")
					
			elif permission_delete == "city":
				try:
	
					country_list = dict1.keys()
					print(country_list)
					country_choice = input("Which country you want to Delete please Enter: ")
					state_list = dict1[country_choice].keys()
					print(state_list)
					state_choice = input("Which state you want to Delete please Enter: ")	
					city_list = dict1[country_choice][state_choice]
					print(city_list)
					city_choice = input("Which city you want to Delete please Enter: ")
					
					def delete_city():
						if city_choice in city_list:
							city_list.remove(city_choice)
						else:
							print("You are selected city is not in list")
							
					delete_city()
					
				except:
					print("country or state is not found in list.")	
					
			else:
				print("You are not selected valid permission")	
		delete()
		
		options(dict1)
			
	elif input_choice == 4:
		
		return
		
	else:
	
		print("Not Selected Valid Option")
	
	
	
	
##main	
	
options()
