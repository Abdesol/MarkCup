import os.path
user = os.path.expanduser('~')

from time import sleep
# MarSearch(item name)
class MarSearch():
	global user
	def __init__(self,name):
		self.name = name

	def checkfile(self):
		self.file_path = f"{user}\\Market Ticketing\\{self.name}_val.txt"
		if os.path.isfile(self.file_path):
			file_open = open(self.file_path,'r')
			print('Yes')
			return file_open.read()
			
			
		else:
			print('No')
			return False
			
			

