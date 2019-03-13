import re
import sys
from collections import Counter

class WC:
	def __init__(self, filename):
		self.filename = filename
	#Reading file
	def open_file(self, filename):
		with open(filename, 'r') as f:
			file_contents = f.read()
			return file_contents

	def counts(self):
		wc_file = self.open_file(self.filename)

		#Reduce special characters
		words_only = re.sub('\W+', ' ', wc_file)
		word_list = words_only.split()
		words_total = len(word_list)
		print(words_total, "words in total.")

		#Reduce repeating words
		word_freq = list(set(word_list))
		most = Counter(word_list).most_common(1)
		print("Most frequent word: ", most)
		for word in word_freq:
			print(word + ": " + str(word_list.count(word)) + "\n")
if __name__ == '__main__':
	#takes a file name as command line argument
	file = WC(sys.argv[1])
	WC.counts(file)
