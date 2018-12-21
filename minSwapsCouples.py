# https://leetcode.com/problems/couples-holding-hands/

class Solution(object):
	def minSwapsCouples(self, row):
		nswaps = 0
		for i in range(0, len(row) - 2, 2):
			if row[i] % 2 == 0:
				match = row[i] + 1
			else:
				match = row[i] - 1

			j = i + 1
			while row[j] != match:
				j += 1

			if j != i + 1:
				nswaps += 1
				row[i + 1], row[j] = row[j], row[i + 1]

		return nswaps

 
