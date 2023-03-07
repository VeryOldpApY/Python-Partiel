def exercice2():
	print("Rentrer A > ", end="")
	A = input()
	print("Rentrer B > ", end="")
	B = input()
	print("Rentrer N > ", end="")
	N = input()
	if A.isnumeric() and B.isnumeric() and N.isnumeric():
		suite(int(A), int(B), int(N))


def suite(A, B, N):
	n = 0
	unn = A
	un = B
	while n != N:
		un = (un + unn) / 2
		unn = 2 / (1 / unn + 1 / un)
		n += 1
	print("a =", A, "b =", B, "n =", n, "=> suite = (", unn, ", ", un, ")")
