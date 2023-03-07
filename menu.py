from Exercice.Exercice1 import exercice1
from Exercice.Exercice2 import exercice2
from Exercice.Exercice3 import exercice3


def menu(exercice):
	match exercice:
		case 1:
			exercice1()
		case 2:
			exercice2()
		case 3:
			exercice3()
		case _:
			print("Exercice inconnu")
			