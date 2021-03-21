import numpy as np
import random
import sympy
import itertools 

x = sympy.symbols('x')

b = 0
# g = x**8 - x

def getList(s):
	return list(itertools.product([0, 1], repeat=s))

# def polydiv(f,g):
# 	for i in g:
# 	new_g = x**indexof
# 	return sympy.div(f,new_g)[1]

# a = x**2+x+1
# d=x**4-x
# if(a == sympy.gcd(a,d)):
# 	print('yes')
# polylist = list(itertools.product([0, 1], repeat=3))


# for i in range(3):
def irreducible(poly):
	lst = getList(9)
	for each in lst:
		g = each[0] + each[1]*x + each[2]*x**2 + each[3]*x**3 + each[4]*x**4 + each[5]*x**5 + each[6]*x**6 + each[7]*x**7 + each[8]*x**8
		if(g != 0 and g != 1 and poly != g):
			# print(poly, g, "===", sympy.div(poly,g))
			if(sympy.div(poly,g)[1] == 0):
				# print(poly, g, "===", sympy.div(poly,g))
				return 0
	return 1



def run():
	for val in polylist:
		a = val
		# print(a)
		# f = x**3 + a[2]*x**2 + a[1]*x + a[0]

		# print(f, list(sympy.factor_list(f)[1][0]))
		if(list(sympy.factor_list(f)[1][0]) == f):
			print(f)
			return
		# for i in range(3):
		# 	newlist = getList(i)
		# 	for poly in newlist:
		# 		if(polydiv(f,list(poly),i) == 0):
		# 			print('reducible')
		# 			return
		# print(f)
		# print('irreducible')
		# return


# run()

	# if(sympy.gcd(f,g) == f):
# 		print(f)

while (b==0):
	choicelist = [0, 1]
	a = random.choices(choicelist, weights = [1, 1], k = 8)
	# if(a == [0,0,0,1,1,1,1,0]):
# 		# print('yes')
# 		# b =1
# 	# a=[1,0,1,1,1,0,0,0]
# 	# values = [0,1]
# 	# com = itertools.combinations_with_replacement(values, 4)
# 	print(lst[0][0])
# 	for val in lst:
# 		print(*val)
# 	b=1	
	f = x**8 +a[7]*x**7 +a[6]*x**6 +a[5]*x**5 + a[4]*x**4 + a[3]*x**3 + a[2]*x**2 + a[1]*x + a[0]
	if(irreducible(f)):
		b=1
		print(f, " is irreducible")
		# print(sympy.div(x**256-x,f))



# print(f)
# 	# ans = sympy.gcd(f,g)
# 	# print(ans)
# 	# b = 1
	# if(ans == f):
		# b=1
		# print(f)