from Materiel import Materiel


class Ecran(Materiel):
	taille = ""
	
	def __init__(self, num, taille):
		super().__init__("Ecran", num)
		self.taille = taille
	
	def __str__(self):
		print("Materiel :", self.type, "[", self.num, "]\n* Taille ", self.taille)
