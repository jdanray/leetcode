# https://leetcode.com/problems/split-array-into-fibonacci-sequence/ 

class Solution(object):
	def splitIntoFibonacci(self, num):
		def split(i, seq):
			if i >= len(num):
				if len(seq) < 3:
					return []

				for j in range(2, len(seq)):
					if seq[j] != seq[j - 1] + seq[j - 2]:
						return []

				return seq

			"""
			Concatenate num[i] to seq[-1], OR
			Append num[i] to seq
			Note: If seq[-1] == 0 or n >= 2**31, you cannot concatenate
			"""

			# append
			if len(seq) < 3 or seq[-1] == seq[-2] + seq[-3]:
				app = split(i + 1, seq + [int(num[i])])
				if app:
					return app

			# concatenate
			if seq and seq[-1] != 0:
				n = seq[-1] * 10 + int(num[i])
				if n < 2**31:
					con = split(i + 1, seq[:-1] + [n])
					if con:
						return con

			return []

		return split(0, [])
