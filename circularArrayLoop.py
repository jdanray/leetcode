# https://leetcode.com/problems/circular-array-loop/

class Solution(object):
	def circularArrayLoop(self, nums):
		seen = set()
		stack = [[i, set(), n > 0] for i, n in enumerate(nums)]
		while stack:
			u, path, fore = stack.pop()

			v = (u + nums[u]) % len(nums)
		
			if (nums[v] < 0 and fore) or (nums[v] > 0 and not fore):
				continue		
	
			if v in path and len(path) > 1:
				return True

			if v not in seen:
				seen.add(v)
				stack.append([v, path | {v}, fore])

		return False
