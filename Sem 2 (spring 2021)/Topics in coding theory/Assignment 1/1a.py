import random
import sympy
import itertools 
from sympy import GF

#variable of the polynomial
x = sympy.symbols('x')

#defined to run the while loop
b = 0

#Returns a list of all possible polynomials over F2(X) upto degree s
#Will return 2^s binary strings
def listgenerator(s):
	return list(itertools.product([0, 1], repeat=s))

#Returns 0 if a polynomail is redducible and 1 otherwise
def GetIrreducible(poly):
	lst = listgenerator(8)
	for each in lst:
		g = each[0] + each[1]*x + each[2]*x**2 + each[3]*x**3 + each[4]*x**4 + each[5]*x**5 + each[6]*x**6 + each[7]*x**7
		if(g != 0 and g != 1 and poly != g):
			if(sympy.div(poly,g, domain=GF(2, symmetric=False))[1] == 0):
				return 0
	return 1

#program starts here
#array a picksout the coefficients randomly from F2
#Then we check if the random polynomial of degree 8 is Irreducible or not
#If it is, we print it and get out of the loop
#This wil print the first Irreducible polynomial it find
while (b==0):
	choicelist = [0, 1]
	a = random.choices(choicelist, weights = [1, 1], k = 7)
	f = x**7 +a[6]*x**6 +a[5]*x**5 + a[4]*x**4 + a[3]*x**3 + a[2]*x**2 + a[1]*x + a[0]
	if(GetIrreducible(f)):
		b=1
		print(f, " is Irreducible")