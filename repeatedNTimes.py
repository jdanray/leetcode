# https://leetcode.com/contest/weekly-contest-116/problems/n-repeated-element-in-size-2n-array/

class Solution(object):
	def repeatedNTimes(self, A):
		seen = set()
		for a in A:
			if a in seen:
				return a
			seen.add(a)
