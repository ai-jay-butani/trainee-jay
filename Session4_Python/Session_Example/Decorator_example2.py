#Factorial using recursion

def fac(num):
	
	if num == 0:
		return 1
	
	return num*fac(num-1)

number = int(input("Enter Number: "))
print(f"Factorial of {number} is: ",fac(number))
