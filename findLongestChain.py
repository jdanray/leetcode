# https://leetcode.com/problems/maximum-length-of-pair-chain/

# doesn't assume that pairs is non-empty
class Solution(object):
	def findLongestChain(self, pairs):
		pairs = sorted(pairs, key=lambda p: p[1])
		tail = -float('inf')
		res = 0
		for (l, r) in pairs:
			if tail < l:
				tail = r
				res += 1
		return res

class Solution:
	def findLongestChain(self, pairs):
		pairs = sorted(pairs, key=lambda p: p[1])
		tail = pairs[0][1]
		m = 1
		for (a, b) in pairs:
			if tail < a:
				tail = b
				m += 1
		return m


class Solution(object):
	def findLongestChain(self, pairs):
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

"""
--------------------------------------------------------------
The following is some thinking that I did to determine that "Maximum Length of Pair Chain" has a greedy solution. I have lightly edited the original freewrite.
----------------------------------------------------------------
Clarifying the problem
-----------------------------------------------
0) Definitions

Def. A pair is a list of two ints -- eg, [2, 5]
Note: The first int in a pair is always smaller than the second int. Ie, for each [a, b], a < b.

Def. 
[c, d] follows [a, b] iff b < c
[a, b] -> [c, d] iff b < c

Def. A chain of pairs is a list of pairs, chain = [pairs[i], pairs[j], ..., pairs[m]], such that chain[i][1] < chain[i + 1][0]
--------------------------------------------------------
1) Preconditions 

PAIRS is a list of N pairs
--------------------------------------------------------
2) Postconditions

M is the length of a maximum-length chain
--------------------------------------------------------
Analysis
------------------------------------------------------
It is often helpful to think of an optimization problem in terms of a sequence of choices. The problem statement says, "You can select pairs in any order." So, it's easy to see how the solution of a problem consists of making a choice. You make a choice of which pair to include in the solution.

In the general case, a chain of pairs will consist of several choices. To form the chain, you choose pairs[i], and then pairs[j], and then pairs[k], etc, etc. But don't think of ALL the choices that need to be made. That is overwhelming, and it's hard to imagine what's going on when there are so many things to imagine. 

Instead, think of ONE choice -- the FIRST choice. Which pair do I choose?(*)

DP tries every pair and picks one that will lead to a globally optimal solution. The problem statement says that 1 <= len(pairs) <= 1000. So, the problem instances might be small enough that a brute-force approach could work.

However, I get the feeling that a greedy algorithm will work. But I have to investigate that question.

I need to use CLRS, et al, to organize my thinking.

Organize how? I picture a web. But thoughts take place in time, so they're sequential. So, what do I think first? Then second? Etc, etc.

I need to consider two questions, in this order:
------------------------------------------------------------------------
1. Does this problem have the greedy-choice property?

What do I do to determine this?!

OK--First of all, what are the candidates for the greedy choice?

A. The pair [a, b] with the smallest a
B. The pair [a, b] with the smallest b

I think that we want to go with B. A pair [c, d] can follow [a, b] only if b < c. So, I think that, to maximize our chances that we'll get a long chain, we'll want to find the [a, b] with the smallest b. Now I've just got to decide whether that's true.

It is true.

Say that we have an optimal solution that doesn't contain the greedy choice:

[a, b] -> [c, d] -> ... -> [e, f]

[a, b] is the pair with the smallest "finish time" for this particular chain. Our greedy-choice pair [g, h] has the smallest "finish time" overall. So, h <= b.

By definition, if [c, d] follows [a, b], then b < c. Since h <= b, it must be the case that h < c. So, we can swap [a, b] for [g, h], and not damage the solution's optimality. Therefore, we can transform any optimal solution into a greedy-based solution.
------------------------------------------------------------------------
2. Does this problem have optimal substructure?

Yes. A solution to the problem is

findLongestChain(pairs) = 1 + findLongestChain(pairs - [greedy choice])

If findLongestChain(pairs - [greedy choice]) were suboptimal, then we could cut-and-paste in an optimal subsolution and get a better solution.
---------------------------------------------------------------------
(*) The question "Which pair do I choose?" assumes that I choose some pair. Do I?
You choose no pairs if and only if the list of pairs is empty. 
If the list is empty, then you can't choose any pairs.
If the list isn't empty, then choosing at least one pair will produce a length greater than the one if you had chosen no pairs. And you're always able to choose at least one pair. So, if the list isn't empty, then you will choose some pairs.
---------------------------------------------------------------------
"""
