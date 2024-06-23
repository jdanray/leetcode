# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/ 

"""
l[j] is the longest satisfactory subarray that ends at j. res is the length of the longest l[j].

Assume that l[j-1] is the longest satisfactory subarray that ends at j-1. To find l[j], combine nums[j] and l[j-1].

I want to use a sliding-window approach to compute all l[j]. 

The difficulty is to maintain the maximum absolute difference within l[j].

Let mx be the maximum num in l[j], and mn be the minimum. Then d = mx - mn. We only care if d increases (?). The only way for d to increase is for mx to increase or mn to decrease.

mx increases iff nums[j] > mx. But we care only if nums[j] - mn > limit (?). If nums[j] - mn > limit, then we need to shorten the window nums[i:j] (ie, increase i), until d is no longer g.t. limit. But, if we go this way, we need a way to update mn as we increase i. Similarly for when mx - nums[j] > limit.
"""

class Solution(object):
	def longestSubarray(self, nums, limit):
		i = -1
		mn = []
		mx = []
		res = 0
		for j, n in enumerate(nums):
			heapq.heappush(mn, (n, j))
			heapq.heappush(mx, (-n, j))

			while n - mn[0][0] > limit or mn[0][1] < i:
				m = heapq.heappop(mn)
				if m[1] > i:
					i = m[1]
                    
			while -mx[0][0] - n > limit or mx[0][1] < i:
				m = heapq.heappop(mx)
				if m[1] > i:
					i = m[1]
                    
			res = max(res, j - i)

		return res
