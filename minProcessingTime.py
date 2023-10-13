# https://leetcode.com/problems/minimum-processing-time/ 

class Solution(object):
	def minProcessingTime(self, processorTime, tasks):
		processorTime = sorted(processorTime)
		tasks = sorted(tasks, reverse=True)

		return max([processorTime[i // 4] + t for i, t in enumerate(tasks)])
