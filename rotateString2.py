# https://leetcode.com/problems/rotate-string/submissions/

class Solution(object):
	def rotateString(self, s, goal):
		if len(goal) != len(s):
			return False

		for k in range(len(s)):
			if all(s[(i + k + 1) % len(s)] == goal[i] for i in range(len(s))):
				return True

		return False

class Solution(object):
	def rotateString(self, s, goal):
		return len(goal) == len(s) and any(all(s[(i + k + 1) % len(s)] == goal[i] for i in range(len(s))) for k in range(len(s)))