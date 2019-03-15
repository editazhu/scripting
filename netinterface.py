import os
import sys
import sh
import re

class NetInterfaces:

	sh.ifconfig(_out="/home/edita/scripting/interfaces")

	def __init__(self):
		pass
	def read_write():
		with open("interfaces", 'r', newline='') as f_in:
			net_info = f_in.readlines()
			with open('inet_status.csv','w') as f_out:
				for line in net_info:
					match = re.match(r'[a-z0-9]+', line)
					if match:
						f_out.write(match.group(0))
						f_out.write('\n')
			f_out.close()
		f_in.close()
		
if __name__ == '__main__':
	NetInterfaces.read_write()
