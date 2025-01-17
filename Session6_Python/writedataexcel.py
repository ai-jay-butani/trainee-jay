import pandas as pd
import os

data = {"india":{"guj":["surat","ahm"], "maha":["mumbai","pune"]},"uk":{},"France":{}}

list1 = []


for l1,inner_dict in data.items():
	cnt = 0
	if inner_dict != {}:
		for l2,inner_list in inner_dict.items():
			cnt1 = 0
			if inner_list != []:
				for l3 in inner_list:
					if cnt == 0 and cnt1 == 0:
						list1.append([l1,l2,l3])
					elif cnt1 == 0:
						list1.append(['',l2,l3])
					else:
						list1.append(['','',l3])
					cnt += 1
					cnt1 += 1
			else:
				list1.append([l1,l2,''])
				cnt1 += 1
				cnt += 1
	else: 
		list1.append([l1,'',''])
		
	list1.append(('','',''))
				
		

print(list1)        
df = pd.DataFrame(list1,columns=["country","state","city"])
print(df) 

filename = "Global_Data.xlsx"
path = "/home/odoo/Python_Practice/" + filename

if os.path.exists(path):
	print("file already created.")
	df_existing = pd.read_excel(path)
	print(df)
	
else:          
	df.to_excel(path)      
print("successfully.....")

