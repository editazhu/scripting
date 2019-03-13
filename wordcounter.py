import re
import sys

class WC:
	def __init__(self, filename):
		self.filename = filename

	def open_file(self, filename):
		with open(filename, 'r') as f:
			file_contents = f.read()
			return file_contents

	def counts(self):
		wc_file = self.open_file(self.filename)
		words_only = re.sub('\W+', ' ', wc_file)
		word_list = words_only.split()
		words_total = len(word_list)
		print(words_total, "words in total.")
		
		word_freq = list(set(word_list))
		for word in word_list:
			print(word + ": " + str(word_list.count(word)) + "\n")
if __name__ == '__main__':
	file = WC(sys.argv[1])
	WC.counts(file)
