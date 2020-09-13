# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

class Solution(object):
	def numTriplets(self, nums1, nums2):
		N1 = len(nums1)
		N2 = len(nums2)

		prods1 = collections.Counter()
		for j in range(N1):
			for k in range(j + 1, N1):
				prods1[nums1[j] * nums1[k]] += 1

		prods2 = collections.Counter()
		for j in range(N2):
			for k in range(j + 1, N2):
				prods2[nums2[j] * nums2[k]] += 1

		res = 0
		for i in range(N1):
			res += prods2[nums1[i] ** 2]
		for i in range(N2):
			res += prods1[nums2[i] ** 2]

		return res

# The above program isn't modular and doesn't obey DRY. The program below tries to fix that: 

class Solution(object):
	def numTriplets(self, nums1, nums2):
		def prods(nums):
			N = len(nums)
			p = collections.Counter()
			for j in range(N):
				for k in range(j + 1, N):
					p[nums[j] * nums[k]] += 1
			return p

		def match(p, nums):
			return sum(p[nums[i] ** 2] for i in range(len(nums)))

		return match(prods(nums1), nums2) + match(prods(nums2), nums1)
