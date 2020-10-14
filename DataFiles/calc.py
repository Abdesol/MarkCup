import os
#calc(item name,number of quantity)

class Calc():
	def __init__(self,item,quan,lst):
		self.item = item
		self.quan = quan
		self.lst = lst
	def validity(self):
		import os.path
		user = os.path.expanduser('~')
		self.file_path = f"{user}\\Market Ticketing\\{self.item}_val.txt"
		if os.path.isfile(self.file_path):
			print("File exists")
			pass	
		else:
			return False

	def calcapp(self):
		file = open(self.file_path,'r')
		item_price = float(file.read())
		self.lst = item_price * float(self.quan)
		return f"item:{self.item} ---------- Quantity:{self.quan} ---------- Total:{self.lst}"

	def si_pr(self):
		return self.lst
