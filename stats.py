def word_count(words):
	temp = words.split()
	count = 0
	for i in range(0, len(temp)):
		count += 1
	print(f"Found {count} total words")
	return temp

def char_count(characters):
	new_dict = {}
	for char in characters:
		temp = char
		for c in temp:
			lower_case = c.lower()
			if lower_case in new_dict:
				new_dict[lower_case] += 1
			else:
				new_dict[lower_case] = 1
	#print(new_dict)
	return new_dict

def sort_dict(items):
	temp_list = []
	for i in items:
		temp_dict = {"char": "", "num": 0}
		temp_dict["char"] = i
		temp_dict["num"] = items[i]
		temp_list.append(temp_dict)
	return temp_list

def sorted_for_sure(sorted_dict):
	return sorted_dict["num"]
