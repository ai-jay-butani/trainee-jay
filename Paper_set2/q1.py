'''Write a function to extract words from the sentence that are repeated multiple times, the
function must return value(s).
Display those words with the ‘#’ separator (use the join function).
For example: WORD1 # WORD2 # WORD3'''

def extract_repeted_words(user_input):
	sentence_toword = user_input.split(' ')
	repeted_words = []
	for i in sentence_toword:
		if (user_input.count(i) > 1) and (i not in repeted_words):
			repeted_words.append(i)
			
	return '#'.join(repeted_words)
	
user_input = input("Enter Sentence: ")
print(extract_repeted_words(user_input))
