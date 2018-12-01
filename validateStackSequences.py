# https://leetcode.com/contest/weekly-contest-112/problems/validate-stack-sequences/

class Solution(object):
	def validateStackSequences(self, pushed, popped):
		pushidx = {p: i for i, p in enumerate(pushed)}
		stack = []
		i = 0
		for j in range(len(popped)):
			idx = pushidx[popped[j]]
			if idx >= i:
				while idx >= i:
					stack.append(pushed[i])
					i += 1
			elif not stack or stack[-1] != popped[j]:
				return False
			stack.pop()
		return True
