	
def Decorator(user_input):
	
	def Calculator():
		
		a,b = user_input()
		
		print("Choose + operator for Addition.")
		print("Choose - operator for Subtraction.")
		print("Choose * operator for Multiplication.")
		print("Choose / operator for Divison.")
		print("Choose ^ operator for Power.")
		print("Choose % operator for Modulo.")
		
		choice = input("Enter your choice: ")
		
		match choice:
			
			case '+':
				try:
					print(f"Addition of {a} and {b} is: {a+b}")
				except Exception as e:
					print(f"{e} Exception occur.")
					
			case '-':
				try:
					print(f"Subtraction of {a} and {b} is: {a-b}")
				except Exception as e:
					print(f"{e} Exception occur.")
					
			case '*':
				try:
					print(f"Multiplication of {a} and {b} is: {a*b}")
				except Exception as e:
					print(f"{e} Exception occur.")
					
			case '/':
				try:
					print(f"Divison of {a} and {b} is: {a/b}")
				except Exception as e:
					print(f"{e} Exception occur.")
			
			case '^':
				try:
					print(f"Power of {a} and {b} is: {a**b}")
				except Exception as e:
					print(f"{e} Exception occur.")
					
			case '%':
				try:
					print(f"{a} modulo {b} is: {a%b}")
				except Exception as e:
					print(f"{e} Exception occur.")
					
			case _:
				print("Not a Valid Option.")
	
	
	return Calculator
	

@Decorator	
def user_input():
	num1 = eval(input("Enter First Number: "))
	num2 = eval(input("Enter Second Number: "))
	return num1,num2

#main
import time
start_time = time.time()
user_input()
end_time = time.time()

print("Execution time is: ",end_time-start_time)
