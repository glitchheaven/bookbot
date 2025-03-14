
thisDict = {}
def get_num_words(path):
	sum =0
	with open(path) as f:
		file_contents = f.read()
		for word in file_contents.split():
			sum+=1
			count_letters(word)

	num_words = sum
	print(f"Found {num_words} total words")

def count_letters(word):
	for s in list(word):
		a = s.lower()
		if thisDict.get(a) is not None:
			thisDict[a] +=1
		if thisDict.get(a) is None:
			thisDict[a] =1

def sort_chars(char_dict):
	chars_list = []
	for char, count in char_dict.items():
		chars_list.append({"char": char, "count": count})

	chars_list.sort(reverse=True, key=lambda d: d["count"])

	return chars_list

def main2(path):
	get_num_words(path)
	sorted = sort_chars(thisDict)
	for c in sorted:
		char = c["char"]
		if char.isalpha():
			count = c["count"]
			print(f"{char}: {count}")

