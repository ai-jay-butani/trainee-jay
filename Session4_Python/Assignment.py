
def FindFile(user_input,sub_dir,path=['/']):

	for k,v in sub_dir.items():
		if user_input == k:
			path.append(k+'/')
			path.append("none")
			return 
		elif type(v) == dict:
			path.append(k + '/')
			FindFile(user_input,v,path)
	return path

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

if "none" in ans:
	indexoflist = ans.index("none")
	file_path = ''.join(ans[:indexoflist])
	print(f"File {user_input} found at {file_path}")
else:
	print("File not found in Data.")
