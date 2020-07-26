# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

class Solution(object):
	def numSplits(self, s):
		rcount = collections.Counter(s)
		rdistinct = len(rcount)
        
		lcount = collections.Counter()
		ldistinct = 0

		res = 0
		for c in s:
			rcount[c] -= 1
			if rcount[c] == 0:
				rdistinct -= 1

			lcount[c] += 1
			if lcount[c] == 1:
				ldistinct += 1

			if ldistinct == rdistinct:
				res += 1

		return res 
