from Materiel import Materiel
from Clavier import Clavier
from Ecran import Ecran
from PC import PC

def exercice3():
	print("-----Materiel-----")
	mat = Materiel("Souris", 10540)
	mat.__str__()
	print("\n-----Clavier-----")
	clav = Clavier(10541, 104)
	clav.__str__()
	print("\n-----Ecran-----")
	ecr = Ecran(105445, "100cm x 50cm")
	ecr.__str__()
	print("\n-----PC-----")
	pc = PC(1504, ecr, clav)
	pc.__str__()
	
	fichier = open("Exercice3.txt", "w")
	fichier.write(str(pc.__str__()))
	fichier.close()
	fichier = open("Exercice3.txt", "r")
	print(fichier.read())
	fichier.close()