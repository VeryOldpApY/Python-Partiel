class Materiel:
	type = ""
	num = 0
	
	def __init__(self, type, num):
		self.type = type
		self.num = num

	def __str__(self):
		print("Materiel :", self.type, "[", self.num, "]")
