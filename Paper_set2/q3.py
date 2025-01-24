def extract_number(input_list,output_list):
	for i in input_list:
		if i>=1000 and i<=9999:
			num = i//1000
			if num%2 != 0 and (i%10)%2 == 0 and ((i%3 == 0) or (i%7 == 0)):
				output_list.append(i)
	return output_list


input_list = []
limit_no_list = int(input("Enter no of item which add in list: "))
for i in range(limit_no_list):
	input_user = float(input("Enter string: "))
	input_list.append(input_user)

output_list = []
print(extract_number(input_list,output_list))
