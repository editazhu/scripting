import os
import sys
import sh
import csv

class NetInterfaces:

	sh.ifconfig(_out="/home/edita/scripting/interfaces")

	def __init__(self):
		pass
	def read_write():
		with open("interfaces", 'r') as f_in:
			with open('inet_status.csv','w') as f_out:
				net_info = f_in.readline()
				f_out.write(net_info)
		#f_out.close()
		
if __name__ == '__main__':
	NetInterfaces.read_write()
