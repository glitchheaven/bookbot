from stats import main2
from stats import count_letters
import sys

def main():
	
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path = sys.argv[1]
	
	main2(path)


main()
