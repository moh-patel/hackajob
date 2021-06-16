
class Solution:

	def run(self, N, M):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		sequence = ""
		for i in range(N,M+1):
			if i%3==0 and i%5==0:
				print("FizzBuzz")
				sequence+="FizzBuzz,"
			elif i%3==0:
				print("Fizz")
				sequence+="Fizz,"
			elif i%5==0:
				print("Buzz")
				sequence+="Buzz,"
			else:
				print(i)
				sequence+=str(i)+","
		
		
		return sequence.rstrip(',')