# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

class Solution(object):
	def gcdSum(self, nums):
		mx = -float('inf')
		pre = []
		for n in nums:
			mx = max(mx, n)
			pre.append(math.gcd(n, mx))

		pre = sorted(pre)
		i = 0
		j = len(pre) - 1
		s = 0
		while i < j:
			s += math.gcd(pre[i], pre[j])
			i += 1
			j -= 1

		return s