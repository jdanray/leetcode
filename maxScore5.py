# https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

class Solution(object):
	def maxScore(self, nums):
		return max(math.gcd(*nums) * math.lcm(*nums), *[math.gcd(*(nums[:i] + nums[i + 1:])) * math.lcm(*(nums[:i] + nums[i + 1:])) for i in range(len(nums))])

class Solution(object):
	def maxScore(self, nums):
		N = len(nums)

		res = math.gcd(*nums) * math.lcm(*nums)
		for i in range(N):
			g = -1
			l = -1
			for j in range(N):
				if i != j:
					if g != -1:
						g = math.gcd(g, nums[j])
						l = math.lcm(l, nums[j])
					else:
						g = nums[j]
						l = nums[j]

			score = g * l
			res = max(res, score)

		return res