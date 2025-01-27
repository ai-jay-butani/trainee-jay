#  5. Write a program to create a list of numbers, and extract integer numbers from a list based on the
#  below conditions.
#  a. Thenumber must be 4 digits long i.e (1000 to 9999)
#  b. Thesecond digit of the number must be odd and the last digit must be even.
#  c. Thenumber must be divisible by either 8 or 5.

def extract_number(input_list,output_list):
	for i in input_list:
		if i>=1000 and i<=9999:
			num = i//100
			if (num%10)%2 != 0 and (i%10)%2 == 0 and ((i%8 == 0) or (i%5 == 0)):
				output_list.append(i)
	return output_list


input_list = []
try:
	limit_no_list = int(input("Enter no of item which add in list: "))
	for i in range(limit_no_list):
		input_user = float(input("Enter number: "))
		input_list.append(input_user)
	output_list = []
	print(extract_number(input_list,output_list))
except:
	print("Invalid Input")
