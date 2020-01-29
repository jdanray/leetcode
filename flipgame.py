# https://leetcode.com/problems/card-flipping-game/

"""
There are N cards. There are positive integers printed on the fronts and backs of the cards.

We flip a subset of cards.
for each i in flips:
	backs[i], fronts[i] = fronts[i], backs[i]

We choose one card. Let c be the index of the chosen card.

Consider backs[c]. If all(backs[c] != fronts[i] for i in range(N)), then backs[c] is "good".

What is the smallest number that is "good"?

Let's say we have:

fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]

We flip the 0th card. We consider backs. What is the smallest card in backs that isn't in fronts? (We can keep fronts as a hashset to enable constant-time lookup.)

The problem is that you can flip N cards. So, there are N! permutations to search the smallest card number across.

Well, there is a saving grace. We only have to search through the numbers given. The smallest card number must be a card number. So, we can create fronts + backs, sort it, and then, for each number, try to find a permutation in which it is "good".

I don't think that I need to create a new data structure or do a sort. I think that I can just search the given, input data structures.
"""

class Solution(object):
	def flipgame(self, fronts, backs):
		smallest = float('inf')
		for i in range(len(fronts)):
			for c in [fronts[i], backs[i]]:
				if c < smallest and all(fronts[j] != c or backs[j] != c for j in range(len(fronts))):
					smallest = c
		return smallest if smallest < float('inf') else 0

"""
The idea behind the above program is this:

smallest is the smallest "good" number up to (but not including) the i-th card. For each i-th card, we assume that it has been chosen. If the number printed on the back of the i-th card is smaller than the currently smallest "good" number, then we decide whether it is "good". If it is good, then it becomes the current smallest good number. (Because we can flip cards, we can consider the front of the i-th card as if it were the back of it too.)

We decide whether a number is good by an exhaustive search. We consider each card. We make sure that the number doesn't appear on the front of any card. Since we can flip cards, if a number appears on the front of a card, but not on the card's back, then the number can still be good.

The program is correct, but slow. The time-complexity is O(N**2). We are guaranteed that 1 <= N <= 1000, so the program is fast enough for the test cases, but it wouldn't be fast enough if N were larger. It would help to speed up the procedure for deciding whether a given card number is good. The exhaustive search really slows the program down.

I thought about what it means for a number to be good. A number c is good if c != backs[i] or c != fronts[i] for all 0 <= i < N. So, in other words, c is good if there is no i such that backs[i] == fronts[i] == c. So, before we investigate whether card numbers are good, we can first consider each card and store its number in a hashset if its front and back are the same. Then, when we decide whether a given card number c is good, we just see if c is a member of the hashset. 
"""

class Solution(object):
	def flipgame(self, fronts, backs):
		N = len(fronts)
		smallest = float('inf')
		bothsides = {fronts[i] for i in range(N) if fronts[i] == backs[i]} 
		for i in range(N):
			if fronts[i] < smallest and fronts[i] not in bothsides: 
				smallest = fronts[i]
			elif backs[i] < smallest and backs[i] not in bothsides:
				smallest = backs[i]

		return smallest if smallest < float('inf') else 0

"""
After I solve a problem, I like to examine other people's solutions. I am pleased to discover that the other problem-solvers used my idea, too. And the following implementation is just too slick to not preserve:

class Solution(object):
	def flipgame(self, f, b):
		same = {x for x, y in zip(f, b) if x == y}
		return min([i for i in f + b if i not in same] or [0])

Source: https://leetcode.com/problems/card-flipping-game/discuss/125791/C%2B%2BJavaPython-Easy-and-Concise-with-Explanation
"""
