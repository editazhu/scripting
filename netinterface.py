import os
import sys
import sh
import csv

class NetInterfaces:

	sh.ifconfig(_out="/home/edita/scripting/interfaces")

	def __init__(self):
		pass
	def read_write():
		with open("interfaces", 'r') as f:
			file_content = f.read()
		
			print(file_content)
		
if __name__ == '__main__':
	NetInterfaces.read_write()
