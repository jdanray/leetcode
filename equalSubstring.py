# https://leetcode.com/problems/get-equal-substrings-within-budget/

"""
--------------------------------------------
Preconditions
--------------------------------------------
string s of length N
string t of length N
int maxCost

Changing s[i] to t[i] costs |s[i] - t[i]|. 

You want to change s to t. But you cannot "spend" more than maxCost. 

You might not get to change s[0..N-1] to t[0..N-1].

You might only change s[i..i+k] to t[i..i+k].
--------------------------------------------
Postconditions
--------------------------------------------
m is the length of the largest "transformed" substring. If no substring from s can be changed to a corresponding substring from t, then return 0. 
--------------------------------------
Thoughts
-----------------------------------
How about this? Search for i and k. Return k - i + 1.

Can I apply a sliding-window approach?
--------------------------------------------
"""

class Solution(object):
	def equalSubstring(self, s, t, maxCost):
		N = len(s)
		alpha = {c: i for i, c in enumerate(string.ascii_lowercase)}
		change = {i: abs(alpha[s[i]] - alpha[t[i]]) for i in range(N)}
		i = 0
		j = 0
		res = 0
		cost = 0
		while j < N:
			cost += change[j] 
			while i <= j and cost > maxCost:
				cost -= change[i]
				i += 1
			j += 1
			res = max(res, j - i)
		return res

"""
After I solve a problem, I like to see other people's solutions.

The following solution is simpler and faster.

Source: https://leetcode.com/problems/get-equal-substrings-within-budget/discuss/392837/JavaC%2B%2BPython-Sliding-Window 
"""

class Solution(object):
	def equalSubstring(self, s, t, maxCost):
		i = 0
		for j in range(len(s)):
			maxCost -= abs(ord(s[j]) - ord(t[j]))
			if maxCost < 0:
				maxCost += abs(ord(s[i]) - ord(t[i]))
				i += 1
		return j - i + 1
