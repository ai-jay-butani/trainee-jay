class Shelf:

	def add_shelf(self,no_of_shelf = 0,data={}):
		self.data = data
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
		self.data[shelfName][productName][monthName]["profit"] = []
		for i in range(self.no_of_costPrice):
			cp = float(input("Enter cost price: "))
			self.data[shelfName][productName][monthName]["cp"].append(cp)
			
		for i in self.data[shelfName][productName][monthName]["cp"]:
			self.data[shelfName][productName][monthName]["sp"].append(i + (i*percentage)/100)
			
		for i,j in zip(self.data[shelfName][productName][monthName]["sp"],self.data[shelfName][productName][monthName]["cp"]):
			self.data[shelfName][productName][monthName]["profit"].append(i-j)
			
	def update_saleprice_pershelf(self,df):
		choice_shelfName = input("Enter shelf name: ")
		percentage = int(input("Enter new profit margin: "))
		def iterate_price(x):
			y = []
			for i in x:
				y.append((i + (i*percentage)/100))
			return y
		df.loc[(df["shelf"] == choice_shelfName),"saleprice"] = df["costprice"].apply(iterate_price)
		print("updated successfully.....")
		return df
	
	def update_saleprice_perproduct(self,df):
		choice_productName = input("Enter shelf name: ")
		percentage = int(input("Enter new profit margin: "))
		def iterate_price(x):
			y = []
			for i in x:
				y.append((i + (i*percentage)/100))
			return y
		df.loc[(df["product"] == choice_productName),"saleprice"] = df["costprice"].apply(iterate_price)
		print("updated successfully.....")
		return df
		
	def set_category(self):
		shelfName = input(f"Which shelf you want to add category Please Enter:")
		productName = input("Which product you want to add category please enter: ")
		categoryName = input("Enter Category: ")
		self.data[shelfName][productName]["category"] = categoryName
		
	def get_data(self):
		return self.data
		
	def reset_cost_price(self):
		self.add_cost_sale_price(0,0,"reset")
			
class DataAnalyse:
	def dictionary_convertDataFrame(self,user_dict):
		return pd.DataFrame.from_records(
		    	[
				(level1, level2, level3, level4_dict['cp'], level4_dict['sp'], level4_dict['profit']) 
				for level1, level2_dict in user_dict.items()
				for level2, level3_dict in level2_dict.items()
				for level3, level4_dict in level3_dict.items() if isinstance(level3_dict,dict) if level3 != "category" 
				if level4_dict !={}
		    	],
		    	columns=['shelf', 'product', 'month', 'costprice', 'saleprice', 'profit']
			)
			
	def MinMax_SalePrice(self,df):
		df["min_sp"] = df['saleprice'].apply(lambda x: min(x))
		df["max_sp"] = df['saleprice'].apply(lambda x: max(x))

		minmax_data = df.groupby(['shelf', 'product']).agg(
				min_price = ('min_sp', 'min'),
				max_price = ('max_sp', 'max')
				)
		return minmax_data
		
	def AvgPrice_PerShelfMonth(self,df):
		df["avg_cost"] = df['costprice'].apply(lambda x: sum(x)/len(x))
		df["avg_sale"] = df['saleprice'].apply(lambda x: sum(x)/len(x))	
		df["avg_profit"] = df['profit'].apply(lambda x: sum(x)/len(x))
		
		avg_data_shelf = df.groupby(['shelf','month']).agg(avg_cost = ('avg_cost','sum'),avg_sale = ('avg_sale','sum'),
		avg_profit = ('avg_profit', 'sum'))
		
		return avg_data_shelf
	   	
	def AvgPrice_PerProductMonth(self,df):
		df["avg_cost"] = df['costprice'].apply(lambda x: sum(x)/len(x))
		df["avg_sale"] = df['saleprice'].apply(lambda x: sum(x)/len(x))	
		df["avg_profit"] = df['profit'].apply(lambda x: sum(x)/len(x))
		
		avg_data_product = df.groupby(['product','month']).agg(
				avg_cost = ('avg_cost','sum'),
				avg_sale = ('avg_sale','sum'),
				avg_profit = ('avg_profit', 'sum')
	   			)
		return avg_data_product
	   	
def repeted_obj(obj):
	data = obj.get_data()
	data_analyse = DataAnalyse()
	df = data_analyse.dictionary_convertDataFrame(data)
	return data_analyse, df
		
##main
import pandas as pd

obj = Shelf()
no_of_shelf = int(input("Enter the no of shelf you want to add: "))
obj.add_shelf(no_of_shelf)
no_of_product = int(input("Enter the no of product you want to add: "))
obj.add_product(no_of_product)
no_of_month = int(input("Enter the no of month you want to add: "))
obj.add_month(no_of_month)
no_of_costprice = int(input("Enter the no of cost price you want to add: "))
percentage = int(input("Enter the profit margin: "))
obj.add_cost_sale_price(no_of_costprice, percentage)

while True:
	print("Please Enter 1 for you want add cost price for specific shelf,product and month: ")
	print("Please Enter 2 for update the sale price given product with a given percentage: ")
	print("Please Enter 3 for update the sale price for a given shelf with a given percentage: ")
	print("Please Enter 4 for set a category for specific product: ")
	print("Please Enter 5 for create new shelf: ")
	print("Please Enter 6 for reset cost price: ")
	print("Please Enter 7 for get max-min sale price with shelf name and product name: ")
	print("Please Enter 8 for to display Average cost,sale and profit based on shelf and specific month: ")
	print("Please Enter 9 for to display Average cost,sale and profit based on product and specific month: ")
	print("Please Enter 10 for Exit: ")
	choice = int(input("Enter choice: "))

	if choice == 1:
		no_of_costprice = int(input("Enter the no of cost price you want to add: "))
		percentage = int(input("Enter the profit margin: "))
		obj.add_cost_sale_price(no_of_costprice, percentage)
	elif choice == 2:
		data_analyse, df = repeted_obj(obj)
		df = obj.update_saleprice_perproduct(df)
	elif choice == 3:
		data_analyse, df = repeted_obj(obj)
		df = obj.update_saleprice_pershelf(df)
	elif choice == 4:
		obj.set_category()
	elif choice == 5:
		data = obj.get_data()
		obj.add_shelf(1,data)
	elif choice == 6:
		obj.reset_cost_price()
	elif choice == 7:
		data_analyse, df = repeted_obj(obj)
		print(data_analyse.MinMax_SalePrice(df))
	elif choice == 8:
		data_analyse, df = repeted_obj(obj)
		print(data_analyse.AvgPrice_PerShelfMonth(df))
	elif choice == 9:
		data_analyse, df = repeted_obj(obj)
		print(data_analyse.AvgPrice_PerProductMonth(df))
	elif choice == 10:
		break
	else:
		print("Invalid choice")




				
