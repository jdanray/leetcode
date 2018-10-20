"""
https://leetcode.com/problems/find-and-replace-pattern/description/

PROBLEM STATEMENT:

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
--------------------------------------------------------------
PROBLEM ANALYSIS:

Preconditions:
WORDS is a list of strings
PATTERN is a string
For each 0 <= i < len(WORDS), len(WORDS[i]) == len(PATTERN)

Postcondition:
MATCHES is the sublist of WORDS that matches with PATTERN

A word matches PATTERN if 
[a] there is a permutation p of letters s.t.
[b] if you replace every letter x in pattern with p(x), then you get the word

A permutation of letters is a bijection from letters to letters. So, the problem is to decide, for each word, whether there is a mapping p from the pattern to the word which satisfies the following conditions:

[i] For each letter x in pattern, p(x) maps to some element in word
[ii] p(x) maps to some unique element in word [For any two letters x, y in pattern, if p(x) == p(y), then x == y]
[iii] For each 0 <= i < len(pattern), p(pattern[i]) == word[i]

Approach:

For each word, try to iteratively construct p. If it can't be constructed, then there's no permutation, and word and pattern don't match.

At each iteration, try to assign pattern[i] to word[i]. [That is, try to satisfy conditions [i] and [iii].]
At every iteration, either p(pattern[i]) is defined or undefined.
If p(pattern[i]) is defined, then it must be equal to word[i]. If it's not, then p doesn't exist. [This follows from condition [iii].]
If p(pattern[i]) is undefined, we need to make sure that p doesn't already map to word[i]. [This ensures that condition [ii] holds.]
"""

class Solution(object):
	def findAndReplacePattern(self, words, pattern):
		matches = []
		for word in words:
			match = True
			p = {}
			for i, x in enumerate(pattern):
				if (x in p and p[x] != word[i]) or (x not in p and word[i] in p.values()):
					match = False
					break
				p[x] = word[i]
			if match:
				matches.append(word)
		return matches
