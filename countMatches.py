# https://leetcode.com/problems/count-items-matching-a-rule/ 

class Solution(object):
	rulekeys = ["type","color","name"]
	key2idx = {k: i for i, k in enumerate(rulekeys)}

	def countMatches(self, items, ruleKey, ruleValue):
		idx = self.key2idx[ruleKey]
		return sum(1 if item[idx] == ruleValue else 0)
