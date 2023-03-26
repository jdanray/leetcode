# https://leetcode.com/problems/k-items-with-the-maximum-sum/ 

class Solution(object):
	def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
		res = min(numOnes, k)
		k -= min(numOnes, k)
		k -= min(numZeros, k)
		res -= min(numNegOnes, k)
		return res

class Solution(object):
	def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
		m = min(numOnes, k)
		return m - min(numNegOnes, k - m - min(numZeros, k - m))
