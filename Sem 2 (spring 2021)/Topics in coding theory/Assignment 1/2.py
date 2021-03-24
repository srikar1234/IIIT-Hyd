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

#polynomial mulitplactions
def PolyMultiplications(p1,p2,r,irp):
	for i in range(r):
		p2 = Poly(p1*p2,x,domain=GF(2, symmetric=False)).expr
		p2 = sympy.div(p2,irp,domain=GF(2, symmetric=False))[1]
	return p2

#encoding the msg vector
def isEncodable(n,k,ffield,msg,msg_poly,irp):
	codeword = []
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
#since max n = 50 from the question, we take a polynomial of degree 6 as (2^6 > 50) it cam satisfy all the 3 cases
def run():
	irp = x**6 + x + 1
	ffield = FF(irp,sympy.degree(irp,gen=x))
	beta = x**4 + x + 1
	
	#k =4
	msg = ffield[0:4]
	msg_poly = 1 + PolyMultiplications(beta,x,2,irp)
	print("msg poly",msg_poly)
	codeword = isEncodable(10,4,ffield,msg,msg_poly,irp)
	print("Message", codeword[0:4])
	print("Encode codeword", codeword)

	#k = 10
	msg2 = ffield[0:10]
	msg_poly2 = sympy.expand(beta**4 + x**3*beta**5 + x**9*beta*10)
	msg_poly2 = sympy.div(msg_poly2,irp,domain=GF(2, symmetric=False))[1]
	print("msg poly 2",msg_poly2)
	codeword2 = isEncodable(20,10,ffield,msg2,msg_poly2,irp)
	print("Message 2", codeword2[0:10])
	print("Encode codeword 2", codeword2)

	#k = 25
	msg3 = ffield[0:25]
	msg_poly3 = sympy.expand(beta**20 + x**8*beta**4 + x**12*beta*44 + x**14*beta**30 + x**18*beta**15 + x**23*beta**3)
	msg_poly3 = sympy.div(msg_poly3,irp,domain=GF(2, symmetric=False))[1]
	print("msg poly 3",msg_poly3)
	codeword3 = isEncodable(50,25,ffield,msg3,msg_poly3,irp)
	print("Message 3", codeword3[0:25])
	print("Encode codeword 3", codeword3)
	return

run()