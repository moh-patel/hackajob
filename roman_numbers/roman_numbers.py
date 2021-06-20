class Solution:

	def run(self, n):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		
		n_number = ''
		return self.recursion(n, n_number)
		
	
	def recursion(self, n, n_number):
		if n//1000 >=1:
			m = n//1000
			n_number += 'M'*m
			n-= 1000*m
			return self.recursion(n, n_number)
		elif n//100 >=1:
			c = n//100
			if c <4:
				n_number += 'C'*c
			elif c ==4:
				n_number += 'CD'
			elif c ==5:
				n_number += 'D'
			elif c ==9:
				n_number += 'CM'
			else:
				n_number += 'D' + 'C' * (c-5)
			n-= 100 *c
			return self.recursion(n,n_number)
		elif n//10 >=1:
			x = n//10
			if x <4:
				n_number +='X' *x
			elif x ==4:
				n_number += 'XL'
			elif x == 5:
				n_number += 'L'
			elif x ==9:
				n_number += 'XC'
			else:
				n_number+= 'L'+'X'*(x-5)
			n = n -(10*x)
			return self.recursion(n, n_number)
		elif n//1 >=1:
			i = n//1
			if i < 4:
				n_number+= 'I'*i
			elif i ==4:
				n_number += 'IV'
			elif i ==5:
				n_number += 'V'
			elif i ==9:
				n_number += 'IX'
			else:
				n_number += 'V' + 'I' *(i-5)
			n-= n*i
			return n_number
		else:
			return n_number