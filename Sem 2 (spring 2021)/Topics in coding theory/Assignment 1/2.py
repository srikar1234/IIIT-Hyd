import random
import sympy
import itertools 
from sympy import Poly
from sympy import GF

x = sympy.symbols('x')

#List of all polynomials of degree 8 in F2(X)
def listGenerators(s):
	lst = list(itertools.product([0, 1], repeat=s))
	poly_lst = []
	for each in lst:
		val = 0
		for i in range(s):
			val = val + each[i]*x**i
		poly_lst.append(val)
	return poly_lst

#generating the finite fields with the help of the irreducible polynomial
def FF(irp,d):
	lst = listGenerators(d+1)
	poly_lst = []
	for each in lst:
		each = sympy.div(each,irp,domain=GF(2, symmetric=False))[1]
		if each not in poly_lst:
			poly_lst.append(each)
	return poly_lst

#encoding the msg vector
def isEncodable(n,k,ffield,msg,msg_poly,irp):
	codeword = []
	#copying the k alpha values
	points = msg[:]
	while(len(points) != n):
		point = random.choice(ffield)
		if(point not in points):
			points.append(point)
	#printing the necessary elements of the finite field used in encoding
	print("The alpha values for encoding are:", points)
	for i in range(n):
		val = sympy.expand(msg_poly.subs(x,points[i]))
		val = sympy.div(val,irp,domain=GF(2, symmetric=False))[1]
		codeword.append(ffield.index(val))
	return codeword

#program starts here
#we take any random irp
#since max n = 50 from the question, we take a polynomial of degree 6 as (2^6 > 50) it can satisfy all the 3 cases
#Note: The finite fields arent in order. 
def run():
	irp = x**6 + x**5 + 1
	print("Irreducible polynomial: ", irp)
	#found in a similar manner from 1b.py
	beta = x**4 + x**3 + 1
	print("Beta polynomial: ", beta)
	#finite fields generated randomly
	ffield = FF(irp,sympy.degree(irp,gen=x))
	
	#k =4
	msg = ffield[0:4]
	msg_poly1 = sympy.expand(1 + x*beta**2)
	msg_poly1 = sympy.div(msg_poly1,irp,domain=GF(2, symmetric=False))[1]
	print("Msg poly 1: ",msg_poly1)
	codeword = isEncodable(10,4,ffield,msg,msg_poly1,irp)
	print("Message: ", codeword[0:4])
	print("Encode codeword: ", codeword)
	print("\n")

	#k = 10
	msg2 = ffield[0:10]
	msg_poly2 = sympy.expand(beta**4 + x**3*beta**5 + x**9*beta*10)
	msg_poly2 = sympy.div(msg_poly2,irp,domain=GF(2, symmetric=False))[1]
	print("Msg poly 2: ",msg_poly2)
	codeword2 = isEncodable(20,10,ffield,msg2,msg_poly2,irp)
	print("Message 2: ", codeword2[0:10])
	print("Encode codeword 2: ", codeword2)
	print("\n")

	#k = 25
	msg3 = ffield[0:25]
	msg_poly3 = sympy.expand(beta**20 + x**8*beta**4 + x**12*beta*44 + x**14*beta**30 + x**18*beta**15 + x**23*beta**3)
	msg_poly3 = sympy.div(msg_poly3,irp,domain=GF(2, symmetric=False))[1]
	print("Msg poly 3: ",msg_poly3)
	codeword3 = isEncodable(50,25,ffield,msg3,msg_poly3,irp)
	print("Message 3: ", codeword3[0:25])
	print("Encode codeword 3: ", codeword3)
	return

run()