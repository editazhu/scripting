import os
import sys
import sh
import csv
import re

class NetInterfaces:

	sh.ifconfig(_out="/home/edita/scripting/interfaces")

	def __init__(self):
		pass
	def read_write():
		with open("interfaces", 'r') as f_in:
			net_info = f_in.readlines()
			with open('inet_status.csv','w') as f_out:
				pattern = re.compile(r'[a-z0-9]+')
				inet = set() 
				for line in net_info:
					match = re.match(pattern, line)
					print(match)
					#return re.match object, how to save result?
					#writer = csv.writer(f_out, 'wb')
					#inet.add(writer)
					#writer.writerow(match[1])
			f_out.close()
		f_in.close()
		
if __name__ == '__main__':
	NetInterfaces.read_write()
