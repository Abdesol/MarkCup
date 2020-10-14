import os.path
user = os.path.expanduser('~')
#MarEdit(item name,newPrice)

class MarEdit():
	global user
	def __init__(self,name,price):
		self.name = name
		self.price = price

	def checkfile(self):
		self.file_path = f"{user}\\Market Ticketing\\{self.name}_val.txt"

		if os.path.isfile(self.file_path):
			file_open = open(self.file_path,'w')
			file_open.write(str(self.price))
			print('Good')
			
		else:
			print('NO')
			return False