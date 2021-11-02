# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/ 

class Solution(object):
	def nodesBetweenCriticalPoints(self, head):
		preVal = -1
		firstCrit = -1
		preCrit = -1
		minDist = float('inf')
		idx = 0

		while head and head.next:
			if preVal != -1 and (preVal < head.val > head.next.val or preVal > head.val < head.next.val):
				if firstCrit == -1:
					firstCrit = idx

				if preCrit != -1:
					minDist = min(minDist, idx - preCrit)

				preCrit = idx

			preVal = head.val
			idx += 1
			head = head.next

		if preCrit == firstCrit:
			return [-1, -1]
		else:
			return [minDist, preCrit - firstCrit]
