# https://leetcode.com/problems/maximal-score-after-applying-k-operations/ 

class Solution(object):
	def maxKelements(self, nums, k):
		nums = [-float(n) for n in nums]
		heapq.heapify(nums)
		res = 0
		for _ in range(k):
			n = heapq.heappop(nums)
			n = abs(n)
            
			res += n
            
			n = -math.ceil(n / 3)
			heapq.heappush(nums, n)

		return int(res)
