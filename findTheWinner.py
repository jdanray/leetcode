# https://leetcode.com/problems/find-the-winner-of-the-circular-game/ 

class Solution(object):
	def findTheWinner(self, n, k):
		friends = collections.deque([i for i in range(1, n + 1)])
		while len(friends) > 1:
			for i in range(k):
				friends.append(friends.popleft())
                
			friends.pop()
            
		return friends[0]
