# https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution(object):
	def minSetSize(self, arr):
		half = len(arr) // 2
		count = collections.Counter(arr)
		keys = sorted(count, key=lambda k: count[k], reverse=True)
		K = 0
		while half > 0:
			half -= count[keys[K]]
			K += 1
		return K
