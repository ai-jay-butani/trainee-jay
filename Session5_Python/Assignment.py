#Banking System
class BankAccount:
	def __init__(self,holder,number,balance=0):
		self.account_number = number
		self.holder = holder
		self.balance = balance

	def providebankaccount(self,data,type_of_account):
		data[self.account_number] = []
		data[self.account_number].extend([self.balance,type_of_account])
		
	def deposite(self,deposite_amount):
		self.add_amount = deposite_amount
		self.balance = self.balance + self.add_amount
		print("Deposite Succesfully.")
		return self.balance
		
	def withdrawal(self,withdraw_amount):
		self.withdraw_amount = withdraw_amount
		if self.balance < self.withdraw_amount:
			print("Your withdrwal amount is grater than balance.")
		else:
			self.balance = self.balance - self.withdraw_amount
			print("Withdraw Succesfully....")
		return self.balance
		
	def display_balance(self):
		print("Balance is: ",self.balance)
		

class SavingAccount(BankAccount):
	
	def __init__(self,name,number,balance=0):
		super().__init__(name,number,balance)

	def interest_calculation(self,rate,time):
		ans = (self.balance*rate*time)/100
		return ans
		
	def add_interest(self):
		rate = 3
		time = eval(input("Enter time for interest in year: "))
		ans = self.interest_calculation(rate,time)
		interest_balance = self.balance + ans
		print("After apply interest rate to your current balance the balance amount is: ",interest_balance)
		

class CurrentAccount(BankAccount):
	
	def __init__(self,name,number,balance=0):
		super().__init__(name,number,balance)

	def overdraft(self):
		self.overdraft_limit = 20000
		print(f"Overdraft limit is {self.overdraft_limit}")
		
	def withdrawal(self, withdraw_amount):
		self.withdraw_amount = withdraw_amount
		self.overdraft()
		if 0<= self.withdraw_amount <= self.balance + self.overdraft_limit:
			self.balance = self.balance - self.withdraw_amount
			print("Withdraw Successfully")
		else:
			print("Your Balance is lower than overdraft limit plus balance.")
			
		return self.balance
	
def banking_options(obj=None,data={}):
	print("Enter 1 for Create Saving Account: ")
	print("Enter 2 for Create Current Account: ")
	print("Enter 3 for Deposite Amount: ")
	print("Enter 4 for Withdraw Amount: ")
	print("Enter 5 for check balance: ")
	print("Enter 6 for check interest amount: ")
	print("Enter 7 for check overdraft amount: ")
	print("Enter 8 for Exit")				
	choice = int(input("Enter your choice: "))
	
	if choice != 8:
		holder_name = input("Give your holder name: ")
		account_number = input("Enter Account Number in 10 digit: ")
		if len(account_number) == 10 and account_number.isdigit():
			pass
		else:
			print("Account Number is not valid")
			banking_options(obj,data)
			return
		
	if choice == 1:
		if obj == None or (account_number not in data.keys())	:
			sav_obj = SavingAccount(holder_name,account_number)
			sav_obj.providebankaccount(data,"saving")
		else:
			print("Account is already created.")
			sav_obj = SavingAccount(holder_name,account_number,data[account_number][0])
		banking_options(sav_obj,data)
		return

	elif choice == 2:	
		if obj == None or account_number not in data.keys():
			curr_obj = CurrentAccount(holder_name,account_number)
			curr_obj.providebankaccount(data,"saving")
		else:
			print("Account is already created.")
			curr_obj = CurrentAccount(holder_name,account_number,data[account_number][0])
		banking_options(curr_obj,data)
		return
	
	elif choice == 3:
		depo_amt = eval(input("Please Enter Deposite amount: "))
		amount = obj.deposite(depo_amt)
		data[account_number][0] = amount
		banking_options(obj,data)
		return

	elif choice == 4:
		withdraw_amount = eval(input("Please Enter Withdraw amount: "))
		amount = obj.withdrawal(withdraw_amount)
		data[account_number][0] = amount
		banking_options(obj,data)
		return
	
	elif choice == 5:
		obj.display_balance()
		banking_options(obj,data)
		return
		
	elif choice == 6:
		try:
			obj.add_interest()
		except:
			print("This is not valid Type of account to check this option.")
		finally:
			banking_options(obj,data)
			return
	
	elif choice == 7:
		try:
			obj.overdraft()
		except:
			print("This is not valid Type of account to check this option.")
		finally:
			banking_options(obj,data)
			return
	
	elif choice == 8:
		return
	else:
		print("Not a Valid Choice.")
		banking_options(obj,data)
				
#main
banking_options()
		
