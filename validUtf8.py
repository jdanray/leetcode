# https://leetcode.com/problems/utf-8-validation/ 

class Solution(object):
	def validUtf8(self, data):
		N = len(data)

		i = 0
		while i < N:
			# count leading 1's
			n = 0
			for _ in range(8):
				if data[i] & 1 == 1:
					n += 1
				else:
					n = 0
				data[i] >>= 1

			# n is valid only for values 0,2,3,4
			if n == 1 or n > 4:
				return False

			# check that the next n-1 ints begin with '10'
			stop = i + n
			i += 1
			while i < stop and i < N and 128 <= data[i] < 128 + 64:
				i += 1

			# not enough ints began with '10'
			if i < stop:
				return False

		return True
