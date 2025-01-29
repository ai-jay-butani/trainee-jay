#Banking System
class BankAccount:
	
	def __init__(self,holder,number,balance=0):
		
		self.account_number = number
		self.holder = holder
		self.balance = balance

	def providebankaccount(self,data,type_of_account):

		if self.account_number in list(data.keys()):
			self.providebankaccount(data)
		else:
			data[type_of_account][self.account_number] = self.balance
			print("Your Account Number is: ",self.account_number)
		
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

	def add_overdraft(self):
		self.overdraft_limit = 20000
		
	def withdrawal(self, withdraw_amount):
		self.withdraw_amount = withdraw_amount
		self.add_overdraft()
		if 0<= self.withdraw_amount <= self.balance + self.overdraft_limit:
			print(f"Overdraft loan is {self.withdraw_amount - self.balance}")
			self.balance = self.balance - self.withdraw_amount
			print("Withdraw Succesfully.")
			

		return self.balance

def banking_options(obj,type1):
		if choice == 1:
			depo_amt = eval(input("Please Enter Deposite amount: "))
			amt = obj.deposite(depo_amt)
			data[type1][account_number] = amt

		elif choice == 2:
			withdraw_amount = eval(input("Please Enter Withdraw amount: "))
			amt = obj.withdrawal(withdraw_amount)
			data[type1][account_number] = amt

		elif choice == 3:
			obj.display_balance()
		
		elif choice == 4:
			sav_obj.add_interest()
		elif choice == 5:
			break
		else:
			print("Invalid choice")
		
#main
data = {"saving":{},"current":{}}

while True:
	print("Enter 1 for Saving Account: ")
	print("Enter 2 for Current Account: ")
	print("Enter 1 for Deposite Amount: ")
	print("Enter 2 for Withdraw Amount: ")
	print("Enter 3 for check balance: ")
	print("Enter 4 for check interest amount: ")
	print("Enter 5 for Exit")		
			
	choice = int(input("Enter your choice: "))

	if choice == 1:
		type_account = input("What is type of account saving or current please enter: ").lower()
		holder_name = input("Give your holder name: ")
		account_number = input("Enter Account Number in 10 digit: ")
		while len(account_number) != 10:
			print("Account Number is not valid")
			account_number = input("Enter Account Number in 10 digit: ")
		if type_account == "saving":
			if account_number in list(data["saving"].keys()):
				sav_obj = SavingAccount(holder_name,account_number,data["saving"][account_number])
				banking_options(sav_obj,"saving")	
			else:
				print("Your saving account is not created firt you create your account.")
		
		elif type_account == "current":
			if account_number in list(data["current"].keys()):
				curr_obj = CurrentAccount(holder_name,account_number,data["current"][account_number])

				banking_options(curr_obj,"current")

			else:
				print("Your current account is not exist.")

		else:
			print("please enter valid type of account.")


	elif choice == 2:
		type_open_account = input("Which type of account is create saving or current please enter: ").lower()
		holder_name = input("Give your holder name: ")
		account_number = input("Enter Account Number in 10 digit: ")
		while len(account_number) != 10:
			print("Account Number is not valid")
			account_number = input("Enter Account Number in 10 digit: ")
		
		if type_open_account == "saving":
			sav_obj = SavingAccount(holder_name,account_number)

			sav_obj.providebankaccount(data,"saving")

		elif type_open_account == "current":
			curr_obj = CurrentAccount(holder_name,account_number)

			curr_obj.providebankaccount(data,"current")

		else:
			print("Please enter valid type of account.")

	elif choice == 3:
		break

	else:
		print("Not a Valid Choice.")
		
		
