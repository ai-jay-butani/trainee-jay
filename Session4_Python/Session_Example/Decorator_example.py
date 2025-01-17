def decorator(func):
	def wrapper():
		out = func()
		return out	
	return wrapper
	
def decorator_pattern(func):
	def wrapper(*args):	
		func(*args)
		print(args[0])
		func(*args)
	return wrapper
	
@decorator
def user_input():
	ans = input("Enter string: ")
	return ans
	
@decorator_pattern
def pattern(ans):
	print("*****")
	print("%%%%%")
	
ans = user_input()
pattern(ans)
