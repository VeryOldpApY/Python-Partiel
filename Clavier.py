from Materiel import Materiel


class Clavier (Materiel):
	touches = 0
	
	def __init__(self, num, touches):
		super().__init__("Clavier", num)
		self.touches = touches
	
	def __str__(self):
		print("Materiel :", self.type, "[", self.num, "]\n* Touches ", self.touches)
