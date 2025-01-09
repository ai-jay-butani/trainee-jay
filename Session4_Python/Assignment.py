

def FindFile(user_input,sub_dir,path=["/"],list1=[]):
	
	list_dir = list(sub_dir.keys())
	list_dir.append("none")
	list1.append(sub_dir)
	ans = ""
	
	if user_input in list_dir:
		path.append(user_input)
		return ''.join(path)
	else:
		for i in list_dir:
			try:
				if i == "none":
					del list1[-1]
					path.pop()
		
					
				elif list1[-1][i] == None:	
					pass

				else:
					
					path.append(i+'/')
					sub_dir = list1[-1][i]		
					ans = FindFile(user_input,sub_dir,path,list1)
			except:
				pass
				
			try:
				if ans:
					break
				
			except:
				pass	
	return ans			

#input

directory = {"documents":
		{"work":{"report.doc":None, "file.exe":None},
		 "personal":{"vacation.png":None, "birthday.png":None}
		 }, 
	     "downloads":{"file1.png":None},
	     "songs":
	     	{"MyFavourite":{"file2.mp3":None},
	     	 "AllTimeFavourite":{"file3.mp3":None}
	     	}
	     }
	     
user_input = input("Please Enter filename with extension: ")

ans = FindFile(user_input,directory)
if ans != "":
	print(f"File {user_input} found at {ans}")
else:
	print("File not found in Data.")
