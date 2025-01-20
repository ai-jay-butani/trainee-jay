class Shelf:

	def __init__(self,shelfName,data={}):
		self.shelfName = shelfName
		self.data = data
		self.data[self.shelfName] = {}
		
	def add_product(self,no_of_product=0):
		self.no_of_product = no_of_product
		for i in range(self.no_of_product):
			productName = input("Enter Product Name: ")
			self.data[self.shelfName][productName] = {}
			
	def add_month(self,no_of_month=0):
		self.no_of_month = no_of_month
		productName = input("Which product you want to add month Please Enter: ")
		for i in range(self.no_of_month):
			monthName = input("Enter Month: ")
			self.data[self.shelfName][productName][monthName] = {}
			
	def add_cost_sale_price(self,no_of_costPrice=0,percentage=0,functionality="add"):
		self.no_of_costPrice = no_of_costPrice
		productName = input(f"Which product you want to {functionality} cost price Please Enter: ")
		monthName = input(f"Which month you want to {functionality} cost price Please Enter: ")
		self.data[self.shelfName][productName][monthName]["cp"] = []
		self.data[self.shelfName][productName][monthName]["sp"] = []
		for i in range(self.no_of_costPrice):
			cp = eval(input("Enter cost price: "))
			self.data[self.shelfName][productName][monthName]["cp"].append(cp)
			
		for i in self.data[self.shelfName][productName][monthName]["cp"]:
			self.data[self.shelfName][productName][monthName]["sp"].append(i + (i*percentage)/100)
			
	def update_salePrice(self, percentage):
		pass
		
	def set_category(self):
		productName = input("Which product you want to add category please enter: ")
		categoryName = input("Enter Category: ")
		self.data[self.shelfName][productName]["category"] = categoryName
		
	def get_data(self):
		return self.data
		
	def reset_cost_price(self):
		self.add_cost_sale_price(0,0,"reset")
			
	 
			
##main
		
s1 = Shelf("s1")
s1.add_product(3)
s1.add_month(2)
s1.add_cost_sale_price(3,10)
s1.set_category()
s1.reset_cost_price()
print(s1.get_data())
			
			
			
			
			
			
