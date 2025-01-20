def Decorator(func):
	
	def Calculator():
		print("Choose + operator for Addition.")
		print("Choose - operator for Subtraction.")
		print("Choose * operator for Multiplication.")
		print("Choose / operator for Divison.")
		print("Choose ^ operator for Power.")
		print("Choose % operator for Modulo.")
		print("Choose x for Exits.")
		choice = input("Enter your choice: ")
		
		match choice:
			case '+':
				try:
					a,b = func()
					print(f"Addition of {a} and {b} is: {a+b}")
					Calculator()
				except:
					print("Invalid number.")
					Calculator()		
			case '-':
				try:
					a,b = func()
					print(f"Subtraction of {a} and {b} is: {a-b}")
					Calculator()
				except:
					print("Invalid number.")
					Calculator()		
			case '*':
				try:
					a,b = func()
					print(f"Multiplication of {a} and {b} is: {a*b}")
					Calculator()
				except:
					print("Invalid number.")
					Calculator()		
			case '/':
				try:
					a,b = func()
					print(f"Divison of {a} and {b} is: {a/b}")
					Calculator()
				except ZeroDivisionError:
					print(f"ZeroDivisionError Exception occur.")
					Calculator()
				except:
					print("Invalid number.")
					Calculator()
			case '^':
				try:
					a,b = func()
					print(f"Power of {a} and {b} is: {a**b}")
					Calculator()
				except:
					print("Invalid number.")
					Calculator()
			case '%':
				try:
					a,b = func()
					print(f"{a} modulo {b} is: {a%b}")
					Calculator()
				except:
					print("Invalid number.")
					Calculator()
			case 'x':
				return
			case __:
				print("Not a Valid Option.")
				Calculator()
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

print("Execution time is: ",end_time-start_time," Seconds.")
