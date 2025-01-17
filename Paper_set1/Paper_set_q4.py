#  4. Write a program to extract string elements from a list based on the conditions below.
# a. Thefirst character must be lower and consonant.
# b. Thestring must not contain any number and also does not contain any special character.

def first_filter(input_list,vowels,special_char):
	for i in input_list:
		flag = 0
		if i[0].islower() and i[0] not in vowels:
			for j in i:
		    		if (j in special_char) or (j.isdigit()):
		        		flag = 1
		        		break
		    		else:
		        		flag = 0

			if flag == 0:
		    		print(i)
        
vowels = ['a','e','i','o','u']
special_char = ['!','@','#','$','%','^','&','~','*']
count_str = int(input("How many string you want to enter: "))
input_list = []
for i in range(count_str):
	input_str = input("Enter string: ")
	input_list.append(input_str)
first_filter(input_list,vowels,special_char)
