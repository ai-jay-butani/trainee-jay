class Shelf:

	def add_shelf(self,no_of_shelf = 0):
		self.data = {}
		for i in range(no_of_shelf):
			shelfName = input("Enter shelf name: ")
			self.data[shelfName] = {}
		
	def add_product(self,no_of_product=0):
		self.no_of_product = no_of_product
		shelfName = input("Which shelf you want to add product Please Enter:")
		for i in range(self.no_of_product):
			productName = input("Enter Product Name: ")
			self.data[shelfName][productName] = {}
			
	def add_month(self,no_of_month=0):
		self.no_of_month = no_of_month
		shelfName = input("Which shelf you want to add month Please Enter:")
		productName = input("Which product you want to add month Please Enter: ")
		for i in range(self.no_of_month):
			monthName = input("Enter Month: ")
			self.data[shelfName][productName][monthName] = {}
			
	def add_cost_sale_price(self,no_of_costPrice=0,percentage=0,functionality="add"):
		self.no_of_costPrice = no_of_costPrice
		shelfName = input(f"Which shelf you want to {functionality} cost price Please Enter:")
		productName = input(f"Which product you want to {functionality} cost price Please Enter: ")
		monthName = input(f"Which month you want to {functionality} cost price Please Enter: ")
		self.data[shelfName][productName][monthName]["cp"] = []
		self.data[shelfName][productName][monthName]["sp"] = []
		for i in range(self.no_of_costPrice):
			cp = float(input("Enter cost price: "))
			self.data[shelfName][productName][monthName]["cp"].append(cp)
			
		for i in self.data[shelfName][productName][monthName]["cp"]:
			self.data[shelfName][productName][monthName]["sp"].append(i + (i*percentage)/100)
			
	def update_salePrice(self, percentage):
		pass
		
	def set_category(self):
		shelfName = input(f"Which shelf you want to add category Please Enter:")
		productName = input("Which product you want to add category please enter: ")
		categoryName = input("Enter Category: ")
		self.data[shelfName][productName]["category"] = categoryName
		
	def get_data(self):
		return self.data
		
	def reset_cost_price(self):
		self.add_cost_sale_price(0,0,"reset")
			
	 

def dictionary_convertDataFrame(user_dict):
	return pd.DataFrame.from_records(
	    	[
			(level1, level2, level3, level4_dict['cp'], level4_dict['sp']) 
			for level1, level2_dict in user_dict.items()
			for level2, level3_dict in level2_dict.items()
			for level3, level4_dict in level3_dict.items() if isinstance(level3_dict,dict) if level3 != "category" 
			if level4_dict !={}
	    	],
	    	columns=['shelf', 'product', 'month', 'costprice', 'saleprice']
		)

		
##main
import pandas as pd

obj = Shelf()
obj.add_shelf(2)
obj.add_product(2)
obj.add_month(2)
obj.add_cost_sale_price(2,10)
obj.set_category()
obj.add_month(2)
obj.add_cost_sale_price(2,5)
dict1 = obj.get_data()
print(dict1)
df = dictionary_convertDataFrame(dict1)
print(df)

df["min_sp"] = df['saleprice'].apply(lambda x: min(x))
df["max_sp"] = df['saleprice'].apply(lambda x: max(x))

minmax_data = df.groupby(['shelf', 'product']).agg(
		min_price = ('min_sp', 'min'),
		max_price = ('max_sp', 'max')
		)

df["avg_cost"] = df['costprice'].apply(lambda x: sum(x)/len(x))
df["avg_sale"] = df['saleprice'].apply(lambda x: sum(x)/len(x))	

avg_data = df.groupby(['shelf','month']).agg(
		avg_cost = ('avg_cost','sum'),
		avg_sale = ('avg_sale','sum')
	   )

print(avg_data)




		

			
					
