# https://leetcode.com/problems/keys-and-rooms/

class Solution:
	def canVisitAllRooms(self, rooms):
		visit = {0}
		stack = [0]

		while stack:
			rm = stack.pop()

			for k in rooms[rm]:
				if k not in visit:
					visit.add(k)
					stack.append(k)

		return len(visit) == len(rooms)
