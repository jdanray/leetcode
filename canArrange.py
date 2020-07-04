# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution(object):
	def canArrange(self, arr, k):
		count = collections.Counter([n % k for n in arr])
		return count[0] % 2 == 0 and all(count[n] == count[k - n] or n == 0 for n in count)
