# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution(object):
	def maxDiff(self, num):
		a = str(num)
		i = 0
		while i < len(a) and a[i] == '9':
			i += 1

		if i < len(a):
			a = a.replace(a[i], '9')

		b = str(num)
		i = 0
		while i < len(b) and (b[i] == '1' or b[i] == '0'):
			i += 1

		if i == 0:
			b = b.replace(b[i], '1')
		elif i < len(b):
			b = b.replace(b[i], '0')	

		return int(a) - int(b)
