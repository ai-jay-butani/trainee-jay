def Check_no_of_EmptySeat(seats,empty_seat_count = 0):
	for index in range(0,len(seats)-1,3): 
		try:
			if seats[index] == 0 and seats[index+3] == 1:
				seats[index] = 1
				empty_seat_count += 1
			elif seats[index] == 1 and seats[index+3] == 0:
				seats[index+3] = 1
				empty_seat_count += 1
			elif seats[index] == 0 and seats[index+3] == 0:
				seats[index] = 1
				seats[index+3] = 1
				empty_seat_count += 2
		except:
			return empty_seat_count

	return empty_seat_count
		
seats = []
try:
	no_of_item = int(input("Enter no of items which will add to a list in 0 or 1: "))
	if no_of_item >= 1:
		for i in range(no_of_item):
			item = int(input("Enter item: "))
			seats.append(item)
		print("output: ",Check_no_of_EmptySeat(seats))
	else:
		print("please enter at least four items.")
except ValueError:
	print("Not valid input")

