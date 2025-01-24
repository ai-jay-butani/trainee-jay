#check amstrong number or not
num = eval(input("Enter number: "))
digit = len(str(num))
print("digit is: ",digit)

def amstrong_number(temp,num,digit,sum1 = 0):
	while(temp != 0 ):
	    ans = temp%10
	    sum1 += ans**digit
	    temp = temp//10

	if sum1 == num:
	    print(f"{num} is amstrong number.")
	else:
	    print(f"{num} is not amstrong number.")
	    
amstrong_number(num,num,digit)
