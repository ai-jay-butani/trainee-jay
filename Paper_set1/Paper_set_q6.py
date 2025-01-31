class Shelf:

	def add_shelf(self,no_of_shelf = 0,data={}):
		for i in range(no_of_shelf):
			shelfName = input("Enter shelf name: ")
			data[shelfName] = {}
		return data
		
	def add_product(self,no_of_product=0,data={}):
		self.no_of_product = no_of_product
		shelfName = input("Which shelf you want to add product Please Enter:")
		if shelfName in data.keys():
			for i in range(self.no_of_product):
				productName = input("Enter Product Name: ")
				data[shelfName][productName] = {}
		else:
			print("Shelf name is not in data.")
		return data
			
	def add_month(self,no_of_month=0,data):
		self.no_of_month = no_of_month
		shelfName = input("Which shelf you want to add month Please Enter:")
		if shelfName in data.keys():
			productName = input("Which product you want to add month Please Enter: ")
		else:
			print("Shelf name is not in data.")
		
		if productName in data[shelfName].keys():
			for i in range(self.no_of_month):
				monthName = input("Enter Month: ")
				data[shelfName][productName][monthName] = {}
		else:
			print("Product name is not in data.")
		return data
		
	def add_cost_sale_price(self,no_of_costPrice=0,percentage=0,functionality="add",data={}):
		self.no_of_costPrice = no_of_costPrice
		shelfName = input(f"Which shelf you want to {functionality} cost price Please Enter:")
		if shelfName in data.keys():
			productName = input(f"Which product you want to {functionality} cost price Please Enter: ")
		else:
			print("Shelf name is not in data.")
			
		if productName in data[shelfName].keys():
			monthName = input(f"Which month you want to {functionality} cost price Please Enter: ")
		else:
			print("Product name is not in data.")
			
		if monthName in self.data[shelfName][productName].keys():
			data[shelfName][productName][monthName]["cp"] = []
			data[shelfName][productName][monthName]["sp"] = []
			data[shelfName][productName][monthName]["profit"] = []
			for i in range(self.no_of_costPrice):
				cp = float(input("Enter cost price: "))
				data[shelfName][productName][monthName]["cp"].append(cp)
				
			for i in self.data[shelfName][productName][monthName]["cp"]:
				data[shelfName][productName][monthName]["sp"].append(i + (i*percentage)/100)
				
			for i,j in zip(data[shelfName][productName][monthName]["sp"],
					data[shelfName][productName][monthName]["cp"]):
				data[shelfName][productName][monthName]["profit"].append(i-j)
		else:
			print("Month name is not in data.")
		return data
		
	def update_saleprice_pershelf(self,df):
		choice_shelfName = input("Enter shelf name: ")
		if choice_shelfName in df["shelf"]:
			percentage = int(input("Enter new profit margin: "))
			def iterate_price(x):
				y = []
				for i in x:
					y.append((i + (i*percentage)/100))
				return y
			df.loc[(df["shelf"] == choice_shelfName),"saleprice"] = df["costprice"].apply(iterate_price)
			print("updated successfully.....")
		else:
			print("Shelf name is not in data.")
		return df
	
	def update_saleprice_perproduct(self,df):
		choice_productName = input("Enter shelf name: ")
		if choice_productName in df["product"]:
			percentage = int(input("Enter new profit margin: "))
			def iterate_price(x):
				y = []
				for i in x:
					y.append((i + (i*percentage)/100))
				return y
			df.loc[(df["product"] == choice_productName),"saleprice"] = df["costprice"].apply(iterate_price)
			print("updated successfully.....")
		else:
			print("Product name is not in data.")
		return df
		
	def set_category(self,data={}):
		shelfName = input(f"Which shelf you want to add category Please Enter:")
		if shelfName in data.keys():
			productName = input("Which product you want to add category please enter: ")
		else:
			print("Shelf name is not in data.")
			
		if productName in data[shelfName].keys():
			categoryName = input("Enter Category: ")
			data[shelfName][productName]["category"] = categoryName
		else:
			print("Product name is not in data.")
		return data

	def reset_cost_price(self):
		return self.add_cost_sale_price(0,0,"reset")
		
			
class DataAnalyse:
	def dictionary_convertDataFrame(self,user_data):
		return pd.DataFrame.from_records(
		    	[
				(level1, level2, level3, level4_dict['cp'], level4_dict['sp'], level4_dict['profit']) 
				for level1, level2_dict in user_data.items()
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
	   	
def repeted_obj(data):
	data_analyse = DataAnalyse()
	df = data_analyse.dictionary_convertDataFrame(data)
	return data_analyse, df
		
##main
import pandas as pd

obj = Shelf()
while True:
	try:
		no_of_shelf = int(input("Enter the no of shelf you want to add: "))
		obj.add_shelf(no_of_shelf)
		no_of_product = int(input("Enter the no of product you want to add: "))
		obj.add_product(no_of_product)
		no_of_month = int(input("Enter the no of month you want to add: "))
		obj.add_month(no_of_month)
		no_of_costprice = int(input("Enter the no of cost price you want to add: "))
		percentage = int(input("Enter the profit margin: "))
		obj.add_cost_sale_price(no_of_costprice, percentage)
		break
	except:
		print("Input Number is not valid.")
data = {}	
while True:
	print("Please Enter 1 for add shelf: ")
	print("Please Enter 2 for add product: ")
	print("Please Enter 3 for add month: ")
	print("Please Enter 4 for you want add cost price for specific shelf,product and month: ")
	print("Please Enter 5 for update the sale price given product with a given percentage: ")
	print("Please Enter 6 for update the sale price for a given shelf with a given percentage: ")
	print("Please Enter 7 for set a category for specific product: ")
	print("Please Enter 8 for reset cost price: ")
	print("Please Enter 9 for get max-min sale price with shelf name and product name: ")
	print("Please Enter 10 for to display Average cost,sale and profit based on shelf and specific month: ")
	print("Please Enter 11 for to display Average cost,sale and profit based on product and specific month: ")
	print("Please Enter 12 for Exit: ")
	choice = int(input("Enter choice: "))
	
	if choice == 1:
		no_of_shelf = int(input("Enter the no of shelf you want to add: "))
		data = obj.add_shelf(no_of_shelf,data)
	elif choice == 2:
		no_of_product = int(input("Enter the no of product you want to add: "))
		data = obj.add_product(no_of_product,data)
	elif choice == 3:
		no_of_month = int(input("Enter the no of month you want to add: "))
		data = obj.add_month(no_of_month,data)
	if choice == 1:
		no_of_costprice = int(input("Enter the no of cost price you want to add: "))
		percentage = int(input("Enter the profit margin: "))
		data = obj.add_cost_sale_price(no_of_costprice, percentage,data)
	elif choice == 2:
		data_analyse, df = repeted_obj(data)
		df = data_analyse.update_saleprice_perproduct(df)
	elif choice == 3:
		data_analyse, df = repeted_obj(obj)
		df = obj.update_saleprice_pershelf(df)
	elif choice == 4:
		data = obj.set_category(data)
	elif choice == 6:
		data = obj.reset_cost_price(data)
	elif choice == 7:
		data_analyse, df = repeted_obj(data)
		print(data_analyse.MinMax_SalePrice(df))
	elif choice == 8:
		data_analyse, df = repeted_obj(data)
		print(data_analyse.AvgPrice_PerShelfMonth(df))
	elif choice == 9:
		data_analyse, df = repeted_obj(data)
		print(data_analyse.AvgPrice_PerProductMonth(df))
	elif choice == 10:
		break
	else:
		print("Invalid choice")




				
