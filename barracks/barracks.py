


n = 5
k=2

# k = {i:0 for i in range(1, k+1)}
# print(k)
# for i in range(1,n+1):
#     print(i)


import math
rows = math.ceil(n/k)

fact = math.factorial(k)

result = fact ** rows

print(result)

print(result%1000000007)


import math
class Solution:

	def run(self, n, k):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		rows = math.ceil(n/k)
		fact = math.factorial(k)
		result = fact**rows
		
		nr_ways = result%1000000007
		return nr_ways