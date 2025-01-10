#Banking System

class BankAccount:
	
	def __init__(self,number,holder,balance):
		
		self.account_number = number
		self.holder = holder
		self.balance = balance
		
	def deposite(self,deposite_amount):
		
		self.add_amount = add_amount
		self.balance = self.balance + self.add_amount
		print("Deposite Succesfully.")
		
	def withdrawal(self,withdraw_amount):
	
		self.withdraw_amount = withdraw_amount
		self.balance = self.balance - self.withdraw_amount
		print("Withdraw Succesfully.")
		
	def display_balance(self):
		print("Balance is: ",self.balance)
		

class SavingAccount(BankAccount):
	
	def interest_calculation(self,rate,time):
		ans = (self.balance*self.rate*self.time)/100
		return ans
		
	def add_interest(self):
		rate = 3
		time = eval(input("Enter time for interest in year: ")
		ans = self.interest_calculation(rate,time)
		interest_balance = self.balance + ans
		print("After apply interest rate to your current balance the balance amount is: ",interest_balance)
		

class CurrentAccount(BankAccount):
	
	def add_overdraft(self):
		
		self.overdraft_limit = 20000
		return self.overdraft_limit
		
	def withdrawal(self, withdraw_amount):
		self.withdraw_amount = withdraw_amount
		if self.withdraw_amount > self.overdraft_limit:
			print("The withdrwal amount is larger than overdraft limit.")
		else:
			self.balance = self.balance - self.withdraw_amount
			print("Withdraw Succesfully.")
			

		
		
		
		
		
		
		
		
