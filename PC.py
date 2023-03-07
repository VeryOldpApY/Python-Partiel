from Materiel import Materiel
from Clavier import Clavier
from Ecran import Ecran

class PC (Materiel):
	ecran = None
	clavier = None
	
	def __init__(self, num, ecran, clavier):
		super().__init__("PC", num)
		self.ecran = ecran
		self.clavier = clavier
	
	def __str__(self):
		print("Materiel :", self.type, "[", self.num, "]")
		self.ecran.__str__()
		self.clavier.__str__()
		