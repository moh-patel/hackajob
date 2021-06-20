


























def run(index1, index2):
    if index1 > index2:
        return check(index1, index2)
    else:
        return check(index2,index1)


def check(index1, index2):
    index1 = index1//2
    if index1 > index2:
        return check(index1, index2)
    elif index1 == index2:
        return index1//2
    elif index1<index2:
        index2 = index2//2
        if index2 == index1:
            return index1
        else:
            return check(index1,index2)


print(run(25,100))

print(run(11,13))

print(run(10,21))


print(run(13,15))


print(run(10,11))

print(run(8,31))

print(run(13,29))

print(run(13,14))

print(run(6,7))


class Solution:

	def run(self, index1, index2):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		if index1>index2:
			return self.check(index1, index2)
		else:
			return self.check(index2,index1)
		
		
	def check(self,index1,index2):
		index1 = index1//2
		if index1 > index2:
			return self.check(index1, index2)
		elif index1 == index2:
			return index1//2
		elif index1<index2:
			index2 = index2//2
			if index1==index2:
				return index1
			else:
				return self.check(index1,index2)