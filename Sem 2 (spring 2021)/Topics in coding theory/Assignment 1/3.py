import numpy as np
import random
import sympy
import itertools 
from sympy import Poly
from sympy import GF
import re

x = sympy.symbols('x')
b = sympy.symbols('b')

def getList(s):
	lst = list(itertools.product([0, 1], repeat=s))
	poly_lst = []
	for each in lst:
		val = 0
		for i in range(s):
			val = val + each[i]*x**i
		poly_lst.append(val)
	return poly_lst

def Finitefield(irp,d):
	lst = getList(d+1)
	poly_lst = []
	for each in lst:
		each = sympy.div(each,irp,domain=GF(2, symmetric=False))[1]
		if each not in poly_lst:
			poly_lst.append(each)
	return poly_lst

def genF(beta,irp):
	field = []
	field.append(sympy.sympify('0'))
	field.append(sympy.sympify('1'))
	pol = sympy.sympify('1')
	for i in range(62):
		pol = Poly(pol*beta,x,domain=GF(2, symmetric=False)).expr
		pol = sympy.div(pol,irp,domain=GF(2, symmetric=False))[1]
		field.append(pol)
	return(field)


def encode(n,k,ffield,msg_poly,alphas,irp,beta):
	codeword = []
	for i in range(n):
		val = sympy.expand(msg_poly.subs(x,alphas[i]))
		val = sympy.div(val,irp,domain=GF(2, symmetric=False))[1]
		codeword.append(val)
	return codeword


def getMsg(n,k,ffield,msg_poly,alphas,irp,beta):
	msg = []
	for i in range(k):
		val = sympy.expand(msg_poly.subs(x,alphas[i]))
		val = sympy.div(val,irp,domain=GF(2, symmetric=False))[1]
		msg.append(val)
	return msg

def getError(n,k,alphas,err_poly,irp):
	err_pos = sympy.solve(err_poly)
	n_err = []
	for each in err_pos:
		if each < 0:
			each = each*(-1)
		n_err.append(each+1)
	err_pos = list(set(n_err))
	return err_pos


def getRx(codeword,ffield,err):
	for each in err:
		new_val = random.choice(ffield)
		while(codeword[each-1] == new_val):
			new_val = random.choice(ffield)
		codeword[each-1] = new_val
	return codeword

def decode(rx,ffield,alphas,irp,n,k,t,beta):
	print("Decoding...")
	b = sympy.symbols('b')
	y = sympy.symbols('y')
	var_e = sympy.symbols('e:'+str(t))
	var_n = sympy.symbols('n:'+str(n-t))

	E = ''
	for i in range(t):
		E = E + str(var_e[i])+'*y**'+str(i) +' + '
	E = E + "y**"+str(t)
	E = sympy.sympify(E)

	N = ''
	for i in range(n-t-1):
		N = N + str(var_n[i])+'*y**'+str(i) +' + '
	N = N + str(var_n[n-t-1])+"*y**"+str(n-t-1)
	N = sympy.sympify(N)

	eqs = []
	for i in range(n):
		exp1 = sympy.expand(E.subs(y,alphas[i]))
		exp1 = sympy.div(exp1,irp,domain=GF(2, symmetric=False))[1]
		exp2 = sympy.expand(N.subs(y,alphas[i]))
		exp2 = sympy.div(exp2,irp,domain=GF(2, symmetric=False))[1]
		val = sympy.expand(rx[i]*(exp1) - exp2)
		val = sympy.div(val,irp,domain=GF(2, symmetric=False))[1]
		eqs.append(val)
	symbs = []
	for each in var_e:
		symbs.append(each)
	for each in var_n:
		symbs.append(each)
	G,H = sympy.linear_eq_to_matrix(eqs, symbs)
	A_lst = []
	for i in range(n):
		row = G.row(i)
		A_lst.append(row)

	A = np.zeros((n,n+1))
	W = np.zeros(n)
	Ary = []
	for i in range(n):
		arr = []
		for j in range(n):
			c = ffield.index(sympy.div(A_lst[i][j],irp,domain=GF(2, symmetric=False))[1])
			if(c != 0):
				arr.append(sympy.sympify("b**"+str(c-1)))
			else:
				arr.append(sympy.sympify("0"))
			
		Ary.append(arr)
	B = []
	for i in range(n):
		d = ffield.index(sympy.div(H.row(i)[0],irp,domain=GF(2, symmetric=False))[1])
		if(d != 0):
			B.append(sympy.sympify("b**"+str(d-1)))
		else:
			B.append(sympy.sympify("0"))
	A = sympy.Matrix(Ary)
	B = sympy.Matrix(B)
	res = sympy.linsolve((A,B),symbs)
	res = list(list(res)[0])
	print("LE solved")

	ans = []
	for i in range(n):
		string = str(res[i])[1:-1]
		if( string.find(')/(') != -1):
			pos = string.find(')/(') + 3
			v = sympy.sympify(string[:pos-3])
			v = sympy.div(v,sympy.sympify("1"),domain=GF(2,symmetric=False))[0]
			v = sympy.expand(v.subs(b,beta))
			v = sympy.div(v,irp,domain=GF(2,symmetric=False))[1]
			p = sympy.sympify(string[pos:])
			p = sympy.div(p,sympy.sympify("1"),domain=GF(2,symmetric=False))[0]
			p = sympy.expand(p.subs(b,beta))
			p = sympy.div(p,irp,domain=GF(2,symmetric=False))[1]
			if(v):
				z = sympy.div(v,p,domain=GF(2,symmetric=False))[0]
			else:
				z = sympy.sympify("0")
			z = sympy.div(z,irp,domain=GF(2,symmetric=False))[1]
			ans.append(str(ffield.index(z)))
		else:
			if(res[i] != sympy.sympify('0')):
				res[i] = sympy.div(res[i]*b,b,domain=GF(2,symmetric=False))[0]
			z = sympy.expand(res[i].subs(b,beta))
			z = sympy.div(z,irp,domain=GF(2,symmetric=False))[1]
			ans.append(str(ffield.index(z)))

	res = ans
	E = ''
	for i in range(t):
		if(int(res[i])):
			E = E + str((res[i])) + '*y**' + str(i) + " + "
		else:
			E = E + str(res[i]) + '*y**' + str(i) + " + "
		
	E = E + "y**"+str(t)
	E = sympy.sympify(E)
	print('E : ',E)
	N= ''
	for i in range(len(res)-t):
		if(int(res[i+t])):
			N = N + str(int(res[i+t])) + '*y**' + str(i) + " + "
		else:
			N = N + str((res[i+t])) + '*y**' + str(i) + " + "
	N=N[0:-2]
	N = sympy.sympify(N)
	print('N : ',N)
	M,r = sympy.div(N,E)
	if(r != 0):
		print("Error occurred at LE solving. Please try again")
		return
	M = str(M)
	M = M.replace('y','x')
	M = sympy.sympify(M)
	print('M :',M)
	answer = encode(10,4,ffield,M,alphas,irp,beta)
	code_vector = ''
	for each in answer:
		code_vector = code_vector + ' ' + str(ffield.index(each))
	print("Decoded Vector :", code_vector)
	return

def run():
	irp = x**6 + x + 1
	ffield = Finitefield(irp,sympy.degree(irp,gen = x))
	beta = x**5
	ffield = genF(beta,irp)

	b = sympy.symbols('b')

	alphas = ffield[0:10]

	msg_poly = input("Enter message polynomial: You can pick coefficients from 0..255")
	msg_poly = sympy.sympify(msg_poly)
	print("Message Poly is: " + str(msg_poly))
	err_poly = input("Enter error polynomial of max degree of 7:")
	print("Error Poly is: "+err_poly)
	err_poly = sympy.sympify(err_poly)

	
	msg = getMsg(10,4,ffield,msg_poly,alphas,irp,beta)
	msg_vector = ''
	for each in msg:
		msg_vector = msg_vector + ' ' + str(ffield.index(each))
	print("Message vector :",msg_vector)

	codeword = encode(10,4,ffield,msg_poly,alphas,irp,beta)
	code_vector = ''
	for each in codeword:
		code_vector = code_vector + ' ' + str(ffield.index(each))
	print("Codeword Vector :", code_vector)

	err = getError(10,4,alphas,err_poly,irp)
	print('Error at ',err)

	rx = getRx(codeword,ffield,err)
	rx_vector = ''
	for each in rx:
		rx_vector = rx_vector + ' ' + str(ffield.index(each))
	print("Recieved Vector :", rx_vector)

	decode(rx,ffield,alphas,irp,10,4,len(err),beta)

run()