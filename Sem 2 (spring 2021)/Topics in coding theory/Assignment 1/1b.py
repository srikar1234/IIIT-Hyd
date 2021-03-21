import numpy as np
import random
import sympy
import itertools 
from sympy import Poly
# from pyfinite import ffield
from sympy import GF

x = sympy.symbols('x')



def getList(s):
	lst = list(itertools.product([0, 1], repeat=s))
	poly_lst = []
	for each in lst:
		val = 0
		for i in range(s):
			val = val + each[i]*x**i
		poly_lst.append(val)
	return poly_lst


def irreducible(poly,d):
	lst = getList(d+1)
	for g in lst:
		if(g != 0 and g != 1 and poly != g):
			# print(poly, g, "===", sympy.div(poly,g))
			if(sympy.div(poly,g,domain=GF(2, symmetric=False))[1] == 0):
				# print(poly, g, "===", sympy.div(poly,g))
				return 0
	return 1


def Finitefield(irp,d):
	lst = getList(d+1)
	poly_lst = []
	for each in lst:
		each = sympy.div(each,irp,domain=GF(2, symmetric=False))[1]
		if each not in poly_lst:
			poly_lst.append(each)
	return poly_lst

def checkPrim(poly,ffield,irp):
	lst = ffield[:]
	# print(lst)
	new_poly = []
	new_poly = poly
	lst.remove(poly)
	lst.remove(0)
	lst.remove(1)
	for i in range(253):

		new_poly = Poly(poly*new_poly,x,domain=GF(2, symmetric=False)).expr
		new_poly = sympy.div(new_poly,irp,domain=GF(2, symmetric=False))[1]
		if new_poly in lst:
			# print('there')
			lst.remove(new_poly)
			# print(lst)
		else:
			return 0
	if(lst == []):
		new_poly = Poly(poly*new_poly,x,domain=GF(2, symmetric=False)).expr
		new_poly = sympy.div(new_poly,irp,domain=GF(2, symmetric=False))[1]
		print("beta power 255 = ", new_poly)
		return 1



def findprim(irp):
	ffield = Finitefield(irp,sympy.degree(irp,gen=x))
	# print("field --", str(len(ffield)))
	for each in ffield:
		# print(each," ====>")
		if(each !=0 and each!=1 and irreducible(each,sympy.degree(each, gen=x))):
			print("irreducible is", each)
			if(checkPrim(each,ffield,irp)):
				return each				
	# print(field)

def run():
	irp =  x**8 + x**7 + x**6 + x**4 + x**2 + x + 1

	beta = findprim(irp)
	print("Primtive elem beta = ", beta)
	beta34 = beta
	for i in range(33):
		beta34 = Poly(beta*beta34,x,domain=GF(2, symmetric=False)).expr
		beta34 = sympy.div(beta34,irp,domain=GF(2, symmetric=False))[1]
	print("beta34 = ",beta34)
	beta20 = beta
	for i in range(19):
		beta20 = Poly(beta*beta20,x,domain=GF(2, symmetric=False)).expr
		beta20 = sympy.div(beta20,irp,domain=GF(2, symmetric=False))[1]
	print("beta20 = ",beta20)
	beta54 = beta
	for i in range(53):
		beta54 = Poly(beta*beta54,x,domain=GF(2, symmetric=False)).expr
		beta54 = sympy.div(beta54,irp,domain=GF(2, symmetric=False))[1]
	print("beta54 = ",beta54)
	beta2034 = Poly(beta34*beta20,x,domain=GF(2, symmetric=False)).expr
	beta2034 = sympy.div(beta2034,irp,domain=GF(2, symmetric=False))[1]
	print("beta20 * beta34 = ",beta2034)


run()