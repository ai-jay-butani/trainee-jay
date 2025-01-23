def Total_Saleamount(sales_data):
	total = 0
	for i in sales_data:
		total += i["sale_amount"]
	return total

def Avg_Saleamount(length,total):
	return total/length
	
def Highest_Sellingproduct(sales_data):
	list_productid = []
	for i in sales_data:
		list_productid.append(i["product_id"])
		
	max_count = 0
	p_id = 0
	for i in list_productid:
		product_count = list_productid.count(i)
		if product_count > max_count:
			max_count = product_count
			p_id = i
			
	return sales_data[list_productid.index(p_id)]
			
sales_data = [
{"product_id": 101, "product_name": "Smartphone", "sale_amount": 500, "sale_date": "2025-01-01"},
{"product_id": 102, "product_name": "Laptop", "sale_amount": 300, "sale_date": "2025-01-02"},
{"product_id": 101, "product_name": "Smartphone", "sale_amount": 400, "sale_date": "2025-01-03"},
{"product_id": 103, "product_name": "Smartwatch", "sale_amount": 700, "sale_date": "2025-01-04"}
]	
Analyze_Data = {}
total_sale = Total_Saleamount(sales_data)
avg_sale = Avg_Saleamount(len(sales_data),total_sale)
highest_sellingproduct = Highest_Sellingproduct(sales_data)

Analyze_Data["Total Sales"] = total_sale
Analyze_Data["Average Sales"] = avg_sale
Analyze_Data["Highest-Selling Product"] = {"product_id":highest_sellingproduct["product_id"], "product_name":highest_sellingproduct["product_name"]}

print(Analyze_Data)
