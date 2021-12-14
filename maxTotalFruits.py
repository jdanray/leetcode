# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/ 

class Solution(object):
	def maxTotalFruits(self, fruits, startPos, k):
		startIdx = bisect.bisect_left([f[0] for f in fruits], startPos)

		if startIdx >= len(fruits):
			spanRight = []
			rewardRight = []
		else:
			spanRight = [fruits[startIdx][0] - startPos]
			rewardRight = [fruits[startIdx][1]]
			for i in range(startIdx + 1, len(fruits)):
				spanRight.append(spanRight[-1] + fruits[i][0] - fruits[i - 1][0])
				rewardRight.append(rewardRight[-1] + fruits[i][1])

		if startIdx == 0:
			spanLeft = []
			rewardLeft = []
		else:
			spanLeft = [startPos - fruits[startIdx - 1][0]]
			rewardLeft = [fruits[startIdx - 1][1]]
			for i in range(startIdx - 2, -1, -1):
				spanLeft.append(spanLeft[-1] + fruits[i + 1][0] - fruits[i][0])
				rewardLeft.append(rewardLeft[-1] + fruits[i][1])

		def search(spanForward, rewardForward, spanBack, rewardBack):
			# Try to go forward
			res = 0
			for i in range(len(spanForward)):
				if spanForward[i] > k: break

				res = max(res, rewardForward[i])

				# Try to double-back
				remaining = k - spanForward[i] - spanForward[i]
				idx = bisect.bisect_left(spanBack, remaining)
				if idx < len(spanBack) and remaining == spanBack[idx]:
					res = max(res, rewardForward[i] + rewardBack[idx])
				elif idx > 0:
					res = max(res, rewardForward[i] + rewardBack[idx - 1])

			return res

		rightLeft = search(spanRight, rewardRight, spanLeft, rewardLeft)
		leftRight = search(spanLeft, rewardLeft, spanRight, rewardRight)
        
		return max(rightLeft, leftRight)
