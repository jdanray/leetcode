# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution(object):
	def minMaxDifference(self, num):
		n = str(num)

		i = 0
		while i < len(n) and n[i] == '9':
			i += 1

		if i < len(n):
			maxim = n.replace(n[i], '9')
		else:
			maxim = n

		minim = n.replace(n[0], '0')

		return int(maxim) - int(minim)

class Solution(object):
	def minMaxDifference(self, num):
		maxnum = -float('inf')
		minnum = float('inf')
		for d1 in range(10):
			for d2 in range(10):
				p = 1
				orignum = num
				newnum = 0
				while orignum > 0:
					d = orignum % 10
					if d == d1:
						newnum += (d2 * p)
					else:
						newnum += (d * p)
					p *= 10
					orignum //= 10

				maxnum = max(maxnum, newnum)
				minnum = min(minnum, newnum)
                
		return maxnum - minnum
