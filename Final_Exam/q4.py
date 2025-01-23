def get_sentence(nouns,vowel,add_grammer,end):
	for index,word in enumerate(nouns):
		if index == 0 and (word[0] in vowel):
			add_grammer.append("An "+word)
		elif index == 0 and (word[0] not in vowel):
			add_grammer.append("A "+word)
		elif index == end and (word[0] in vowel):
			add_grammer.append("an "+word+".")
		elif index == end and (word[0] not in vowel):
			add_grammer.append("a "+word+".")
		elif word[0] in vowel:
			add_grammer.append("an "+word)
		else:
			add_grammer.append("a "+word)
			
	return ",".join(add_grammer[:-1]) + " and "+ add_grammer[-1]

nouns = []
add_grammer = []
vowel = ['a','e','i','o','u']
try:
	no_of_item = int(input("Enter no of items which will add to a list: "))
	if no_of_item >= 2:
		for i in range(no_of_item):
			item = input("Enter item: ")
			nouns.append(item)
		end = len(nouns)-1
		sentence = get_sentence(nouns,vowel,add_grammer,end)
		print(sentence)
	else:
		print("please enter at least two items.")
except ValueError:
	print("Not valid input")
