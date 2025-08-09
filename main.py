import sys
from stats import word_count
from stats import char_count
from stats import sort_dict
from stats import sorted_for_sure

def get_book_text(get_file_path):
	with open(get_file_path) as f:
		file_contents = f.read()
	return file_contents
	
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	print("----------- Word Count ----------")
	the_book = get_book_text(sys.argv[1])
	the_words = word_count(the_book)
	the_characters = char_count(the_book)
	the_dict = sort_dict(the_characters)
	the_dict.sort(reverse=True, key=sorted_for_sure)
	print("--------- Character Count -------")
	for i in range(0, len(the_dict)):
		if the_dict[i]["char"].isalpha():
			print(f"{the_dict[i]["char"]}: {the_dict[i]["num"]}")
	print("============= END ===============")
main()