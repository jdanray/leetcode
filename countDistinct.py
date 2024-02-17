# https://leetcode.com/problems/k-divisible-elements-subarrays/ 

class Solution(object):
	def countDistinct(self, nums, k, p):
		N = len(nums)

		seen = set()
		for i in range(N):
			c = 0
			sub = []
			for j in range(i, N):
				if nums[j] % p == 0:
					c += 1
					if c > k:
						break

				sub.append(nums[j])
				seen.add(tuple(sub))

		return len(seen)
