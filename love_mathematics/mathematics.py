import math
class Solution:

	def run(self, number):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		
		isSemiprime = False
		for i in range(2, int(math.sqrt(number)) +1):
			while number%i == 0:
				if self.is_prime(i) and self.is_prime(number/i):
					return True
		
		return isSemiprime
	
	
	def is_prime(self, number):
		if number == 0 or number ==1:
			return False
		
		x = abs(number)
		max= int(math.sqrt(x))
		for i in range(2, max+1):
			if (x%i)==0:
				return False
		return True













# def is_prime( input):
#         if input == 0 or input ==1:
#             return False
#         # Your code goes here
#         x = abs(input)
#         max = int(math.sqrt(x))
#         for i in range(2, max+1):
#             if (x%i)==0:
#                 return False
#         return True




# import math

# def is_semiprime(n):

#     semiprime = False
#     # n = 2
#     divisibles = []
#     for i in range(2, int(math.sqrt(n))+1 ):
#         while n % i ==0:
#             if is_prime(i) and is_prime(n/i):
#                 return True
    
#     return False
#         # if len(primes) >=2
#         # break


# numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 25, 26, 29, 31, 33, 34, 35, 37, 38, 39, 41, 43, 46, 47, 49]

# for i in numbers:
#     print(i, is_semiprime(i))