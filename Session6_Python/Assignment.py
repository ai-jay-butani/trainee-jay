##Logic
def options(path,dict1 = {}):
	print("Please Enter 1 for add option")
	print("Please Enter 2 for update option")
	print("Please Enter 3 for Delete option")
	print("Please Enter 4 for Display option")
	print("Please Enter 5 for Saving data in excel and Exit option")
	input_choice = eval(input("Enter Your Choice: "))
	
	def general_list(data,_name,option,add_name=''):
		gen_list = list(data.keys())
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
		
			print(dict1)
			def add_country():
				input_country = input("Enter Country: ")
				input_country = input_country.lower()
				if input_country in dict1.keys():
					print(f"{input_country} is already in data.")
					add_country()
				else:
					if input_country.isalpha():
						dict1[input_country] = {}
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
			
				country_choice,country_list = general_list(dict1,"country","add","state")
				if country_choice in country_list:
					input_state = input("Enter State: ")
					input_state = input_state.lower()
					if input_state in dict1[country_choice].keys():
						print(f"{input_state} is alreday in data.")
						add_state()
					else:
						if input_state.isalpha():
							dict1[country_choice][input_state] = []
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
						country_choice,country_list = general_list(dict1,"country","add","city")
						state_choice,state_list = general_list(dict1[country_choice],"state","add","city")
						if state_choice in state_list:
							input_city = input("Enter City: ")
							input_city = input_city.lower()
							if input_city.isalpha():
								if check_duplicate(dict1[country_choice][state_choice],input_city):
									dict1[country_choice][state_choice].append(input_city)
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
	
		options(path,dict1)	
				
	elif input_choice == 2:
		
		def update():
		
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
							update_city_name = input("Please Enter new city: ")
							update_city_name  = update_city_name.lower()
							if check_duplicate(dict1[country_choice][state_choice],update_city_name):
								dict1[country_choice][state_choice].remove(city_choice)
								dict1[country_choice][state_choice].append(update_city_name)
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
		
		options(path,dict1)
		
	elif input_choice == 3:
		
		def delete():
		
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
				delete()
		delete()
		
		options(path,dict1)
			
	elif input_choice == 4:
		
		print(dict1)
		options(path,dict1)
	
	elif input_choice == 5:
	
		def convertData_to_excelFormat(data,list1 = []):
			for l1,inner_dict in data.items():
				cnt = 0
				if inner_dict != {}:
					for l2,inner_list in inner_dict.items():
						cnt1 = 0
						if inner_list != []:
							for l3 in inner_list:
								if cnt == 0 and cnt1 == 0:
									list1.append([l1,l2,l3])
								elif cnt1 == 0:
									list1.append(['',l2,l3])
								else:
									list1.append(['','',l3])
								cnt += 1
								cnt1 += 1
						else:
							if cnt1 == 0 and cnt == 0:
								list1.append([l1,l2,''])
							else:
								list1.append(['',l2,''])
							cnt1 += 1
							cnt += 1
				else: 
					list1.append([l1,'',''])
					
				list1.append(['','',''])
			return list1

		list_of_details = convertData_to_excelFormat(dict1)      
		df = pd.DataFrame(list_of_details,columns=["country","state","city"])
		df.to_excel(path)
		return
		
	else:
	
		print("Not Selected Valid Option")
		options()
	
	
	
	
##main	
import pandas as pd
import os
import time
start_time = time.time()

filename = "Global_Data.xlsx"
path = filename

if os.path.exists(path):
	file_data = {}
	df_existing = pd.read_excel(path)
	df_existing.fillna('',inplace = True)
	country = df_existing.loc[0,"country"]
	state = df_existing.loc[0,"state"]
	city = df_existing.loc[0,"city"]
	file_data[country] = {}
	if state != '':
		file_data[country][state] = []
	if city != '':
		file_data[country][state].append(city)
	
	for i in range(1,len(df_existing)-1):
		if df_existing.loc[i,"country"] == '' and df_existing.loc[i,"state"] == '' and df_existing.loc[i,"city"] == '':
			country = df_existing.loc[i+1,"country"]
			file_data[country] = {}
			if df_existing.loc[i+1,"state"]!='':
				state = df_existing.loc[i+1,"state"]
				file_data[country][state] = []
		elif df_existing.loc[i,"country"] == '' and df_existing.loc[i,"state"] == '' and df_existing.loc[i,"city"] != '':
			file_data[country][state].append(df_existing.loc[i,"city"])
		elif df_existing.loc[i,"country"] == '' and df_existing.loc[i,"state"] != '' and df_existing.loc[i,"city"] != '':
			if df_existing.loc[i,"state"]!='':
				state = df_existing.loc[i,"state"]
				file_data[country][state] = []
				file_data[country][state].append(df_existing.loc[i,"city"])
		elif df_existing.loc[i,"country"] == '' and df_existing.loc[i,"state"] != '' and df_existing.loc[i,"city"] == '':
			if df_existing.loc[i,"state"]!='':
				state = df_existing.loc[i,"state"]
				file_data[country][state] = []
			
	print(file_data)
	options(path,file_data)
else:
	options(path)

end_time = time.time()
print("Time taken by function: ",end_time-start_time)
