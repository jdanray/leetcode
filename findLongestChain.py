# https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution(object):
	def findLongestChain(self, pairs):
		if not pairs:
			return 0

		pairs = sorted(pairs, key=lambda p: p[0])
		chain = [1 for _ in range(len(pairs))]
		longest = 1
		for i in range(1, len(pairs)):
			for j in range(i):
				if pairs[j][1] < pairs[i][0] and chain[i] < chain[j] + 1:
					chain[i] = chain[j] + 1
					if longest < chain[i]:
						longest = chain[i]
                        
		return longest

# After I solve a problem, I like to look at other solutions. The following is a solution that I liked:

class Solution(object):
	def findLongestChain(self, pairs):
		cur = float('-inf')
		res = 0
		for p in sorted(pairs, key=lambda x: x[1]):
			if cur < p[0]: 
				cur = p[1]
				res += 1
		return res
