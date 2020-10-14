import os.path
user = os.path.expanduser('~')

#class(item name,single item price)

class Marcreate():
	global user
	def __init__(self,name,price):
		self.name = name
		self.price = price
	def validity(self):
		try:
			os.mkdir(f"{user}\\Market Ticketing")
		except:
			pass
		self.file_path = f"{user}\\Market Ticketing\\{self.name}_val.txt"

		if os.path.isfile(self.file_path):
			return False
			
		else:
			print("File Doesn't Exists")

	def savearea(self):
		mark_file = open(self.file_path,"w")
		write_file = f"{self.price}"
		mark_file.write(write_file)
		print("File has been witten")



