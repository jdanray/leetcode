# https://leetcode.com/problems/remove-elements-by-type-and-color/ 

class Solution(object):
	def canRemoveAll(self, types, colors, groupSize):
		stack = []
		for i, t in enumerate(types):
			if stack and t == stack[-1][0] and colors[i] == stack[-1][1]:
				stack[-1][2] += 1
			else:
				stack.append([t, colors[i], 1])

			if groupSize[stack[-1][0]] == stack[-1][2]:
				stack.pop()

		return not stack
