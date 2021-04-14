# https://leetcode.com/problems/exclusive-time-of-functions/ 

class Solution(object):
	def exclusiveTime(self, n, logs):
		stack = []
		res = [0 for _ in range(n)]
		for l in logs:
			fid, act, t = l.split(':')
			fid, t = int(fid), int(t)

			if act == "start":
				if stack:
					cid, start = stack[-1]
					res[cid] += t - start
				stack.append([fid, t])
			else:
				res[fid] += t - stack[-1][1] + 1
				stack.pop()
				if stack:
					stack[-1][1] = t + 1

		return res
