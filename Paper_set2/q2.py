'''Write a program to extract string elements from a list based on the conditions below,
using built-in functions.
a. The first character must capitalize and consonant.
b. The string must not contain any number.'''

def format_string(input_str_list):
	output_list = []
	[output_list.append(string) for string in input_str_list 
	if (string[0] not in vowel) and (string.isalpha()) and (string[0].isupper())]
	return output_list

vowel = {'a','e','i','o','u','A','E','I','O','U'}
input_list = []
try:
	limit_no_list = int(input("Enter no of item which add in list: "))
	for i in range(limit_no_list):
		input_user = input("Enter string: ")
		input_list.append(input_user)

	print(format_string(input_list))
except:
	print("Invalid Input")
		
