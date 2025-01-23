def list_convert_str(list_backward,list_forward,var,end):
	'''in this function jointwo lists and convert it into string using join function.'''
	list_forward.extend(reversed(list_backward))
	print(''.join(list_forward))

var = input("Enter String: ")
start = 0
end = len(var)-1
list_forward = []
list_backward = []

for i in range(0,len(var)):
	
	if var[start].isalpha() and end!=start:
		if var[end].isalpha() and end!=start:
			list_forward.append(var[end])
			list_backward.append(var[start])
			end -= 1
			start += 1
		else:
			list_backward.append(var[end])
			end -= 1
	else:
		list_forward.append(var[start])
		start += 1
	
	if end<=start and len(var)%2 == 0:
		list_backward.append(var[end])
		list_convert_str(list_backward,list_forward,var,end)
		break
	elif end<start and len(var)%2 != 0:
		list_convert_str(list_backward,list_forward,var,end)
		break
		
			
