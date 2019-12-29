# https://leetcode.com/problems/jump-game-iii/

class Solution(object):
	def canReach(self, arr, start):
		seen = set()
		stack = [start]
		while stack:
			index = stack.pop()
			seen.add(index)

			if arr[index] == 0:
				return True

			a = index + arr[index]
			if a < len(arr) and a not in seen:
				stack.append(a)

			b = index - arr[index]
			if b >= 0 and b not in seen:
				stack.append(b)
				
		return False
