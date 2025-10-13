# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

class Solution(object):
	def sumDivisibleByK(self, nums, k):
		freq = collections.Counter(nums)
		return sum(n * freq[n] for n in freq if freq[n] % k == 0)