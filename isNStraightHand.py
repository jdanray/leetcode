# https://leetcode.com/problems/hand-of-straights/

class Solution(object):
	def isNStraightHand(self, hand, W):
		if len(hand) % W != 0:
			return False

		count = collections.Counter(hand)
		keys = sorted(count.keys())
		i = 0
		while i < len(keys):
			m = keys[i]

			if count[m] == 0:
				i += 1
				continue

			for w in range(1, W):
				count[m + w] -= count[m]
				if count[m + w] < 0:
					return False

			count[m] = 0
			i += 1
			
		return True
