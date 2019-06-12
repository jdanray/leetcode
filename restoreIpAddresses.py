# https://leetcode.com/problems/restore-ip-addresses/ 

class Solution(object):
	def restoreIpAddresses(self, S):
		N = 4
		M = 3
		allcombos = []
		stack = [[0, []]]
		while stack:
			i, addr  = stack.pop()

			if len(addr) > N:
				continue

			if i >= len(S):
				if len(addr) == N:
					allcombos = ['.'.join(addr)] + allcombos
				continue

			a = ''
			for j in range(i, i + M):
				if j >= len(S):
					break

				a += S[j]
				if a[0] == '0' and len(a) > 1: 
					break
				if len(a) == 3 and (a[0] > '2' or (a[0] == '2' and (a[1] > '5' or (a[1] == '5' and a[2] > '5')))):
					break

				stack.append([j + 1, addr + [a]])

		return allcombos
