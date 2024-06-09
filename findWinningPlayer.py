# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

class Solution(object):
	def findWinningPlayer(self, skills, k):
		maxim = max(skills)
		m = 0
		w = 0
		for i in range(1, len(skills)):
			if skills[i] > skills[m]:
				m = i
				w = 1
			else:
				w += 1

			if w == k or m == maxim:
				return m

		return m

"""
After I solve a problem, I like to study other people's solutions. I found a solution that is simpler than mine: https://leetcode.com/problems/find-the-winner-of-an-array-game/discuss/768007/JavaC%2B%2BPython-One-Pass-O(1)-Space

Here is my implementation:
"""

class Solution(object):
	def findWinningPlayer(self, skills, k):
		m = 0
		w = 0
		for i in range(1, len(skills)):
			if skills[i] > skills[m]:
				m = i
				w = 0

			w += 1
			if w == k:
				break

		return m
