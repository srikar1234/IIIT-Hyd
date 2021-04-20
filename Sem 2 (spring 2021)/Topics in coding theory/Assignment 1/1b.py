import random
import sympy
import itertools 
from sympy import Poly
from sympy import GF

x = sympy.symbols('x')

#generating all polynomials of degree s from F2(X) 
def listGenerator(s):
	lst = list(itertools.product([0, 1], repeat=s))
	poly_lst = []
	for each in lst:
		val = 0
		for i in range(s):
			val = val + each[i]*x**i
		poly_lst.append(val)
	return poly_lst

#generating the finite field
def FF(irp,d):
	lst = listGenerator(d+1)
	poly_lst = []
	for each in lst:
		each = sympy.div(each,irp,domain=GF(2, symmetric=False))[1]
		if each not in poly_lst:
			poly_lst.append(each)
	return poly_lst

#checking if the element is a primitive element or not
def primitiveCheck(poly,ffield,irp, degree):
	lst = ffield[:]
	new_poly = []
	new_poly = poly
	lst.remove(poly)
	lst.remove(0)
	lst.remove(1)
	for i in range(2**degree - 3):
		new_poly = Poly(poly*new_poly,x,domain=GF(2, symmetric=False)).expr
		new_poly = sympy.div(new_poly,irp,domain=GF(2, symmetric=False))[1]
		if new_poly in lst:
			lst.remove(new_poly)
		else:
			return 0
	if(lst == []):
		new_poly = Poly(poly*new_poly,x,domain=GF(2, symmetric=False)).expr
		new_poly = sympy.div(new_poly,irp,domain=GF(2, symmetric=False))[1]
		print("Beta**255 = ", new_poly)
		new_poly = Poly(poly*new_poly,x,domain=GF(2, symmetric=False)).expr
		new_poly = sympy.div(new_poly,irp,domain=GF(2, symmetric=False))[1]
		print("Beta**256(= Beta)= ", new_poly)
		return 1

#Finding the primitive element here
#Using the Finite field generated from irp
#for each element we do a primitive check
def getPrim(irp):
	ffield = FF(irp,sympy.degree(irp, gen = x))
	for each in ffield:
		if(each !=0 and each!=1):
			if(primitiveCheck(each,ffield,irp, sympy.degree(irp, gen = x))):
				return each				

#program starts from here
#We take any irreducible polynomial of degree 8 which we get from program 1a 
def run():
	irp = x**8 + x**6 + x**5 + x**3 + 1
	print("Irreducible poynomial = ", irp)

	beta = getPrim(irp)
	
	beta34 = beta
	for i in range(33):
		beta34 = Poly(beta*beta34,x,domain=GF(2, symmetric=False)).expr
	beta34 = sympy.div(beta34,irp,domain=GF(2, symmetric=False))[1]
	print("B^34 = ",beta34)
	
	beta20 = beta
	for i in range(19):
		beta20 = Poly(beta*beta20,x,domain=GF(2, symmetric=False)).expr
	beta20 = sympy.div(beta20,irp,domain=GF(2, symmetric=False))[1]
	print("B^20 = ",beta20)
	
	beta54 = beta
	for i in range(53):
		beta54 = Poly(beta*beta54,x,domain=GF(2, symmetric=False)).expr
	beta54 = sympy.div(beta54,irp,domain=GF(2, symmetric=False))[1]
	print("B^54 = ",beta54)
	
	beta2034 = Poly(beta34*beta20,x,domain=GF(2, symmetric=False)).expr
	beta2034 = sympy.div(beta2034,irp,domain=GF(2, symmetric=False))[1]
	print("B^20 * B^34 = ",beta2034)

	print("They are the same!")
run()