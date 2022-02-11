# https://leetcode.com/problems/largest-values-from-labels/

"""
Here is a quick proof that a greedy algorithm will solve this problem:

Let O be the sequence of choices made in an optimal solution. Let G be the sequence of choices made by the greedy algorithm below.

Either O and G are the same, or they are different.

If O and G are the same, then the greedy algorithm makes the sequence of choices that are made in an optimal solution. So, the greedy algorithm is correct. 

Suppose that O and G are different. That means that there is some index j such that O[j] != G[j]. 

We know that G[j] corresponds to the item that (1) is still available for use that (2) has the highest score. So, if O[j] != G[j], then 

(i) O[j] is an invalid, unusable choice, or 
(ii) O[j] doesn't correspond to the highest score available 

If (i) is the case, then O isn't a valid solution. But we assumed that it was a solution. So, it's impossible that O[j] != G[j], because that leads to a contradiction. So, there is no index j where O and G differ. So, O and G are the same, and the greedy algorithm is optimal.

If (ii) is the case, then G produces a greater score than O, after the sum of the items' scores is carried out. But we assumed that O corresponded to an optimal solution. So, G can't produce a greater score than O. So, we have a contradiction. Therefore, O[j] != G[j], and the greedy algorithm is optimal. 
"""

class Solution(object):
	def largestValsFromLabels(self, values, labels, numWanted, useLimit):
		used = collections.Counter()
		valLabs = sorted(zip(values, labels), reverse=True)
		res = 0
		for v, l in valLabs:
			if used[l] < useLimit:
				res += v
				used[l] += 1

				numWanted -= 1
				if numWanted == 0:
					return res

		return res

class Solution(object):
	def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
		count = collections.defaultdict(int)
		vabels = sorted(zip(values, labels), reverse=True)
		s = 0
		n = 0
		for v, l in vabels:
			if n >= num_wanted:
				break

			if count[l] < use_limit:
				s += v
				count[l] += 1
				n += 1

		return s
