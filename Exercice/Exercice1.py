def exercice1():
	print("Rentrer P > ", end="")
	P = input()
	print("Rentrer T > ", end="")
	T = input()
	seuil(float(P), float(T))
	# if P.isdecimal() and T.isdecimal():
	# 	seuil(float(P), float(T))
	# else:
	# 	print("Erreur, P et T doivent être des nombres")
	
	
def seuil(P, T):
	N = 0
	print("|		P|		N|")
	while P < 1000:
		P = P * T
		if P < 1000:
			N += 1
			print("|	", "{:.2f}".format(round(P, 2), "|	", N, "|"))
