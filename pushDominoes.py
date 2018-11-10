# https://leetcode.com/problems/push-dominoes/

class Solution:
	def pushDominoes(self, dominoes):
		state = dict((i, d) for i, d in enumerate(dominoes))
		falling = set(i for i, d in enumerate(dominoes) if d != '.')

		while falling:
			newfalling = set()
			newstate = dict(state)

			for i in falling:
				if state[i] == 'L':
					if i - 1 >= 0 and state[i - 1] == '.':
						if (i == 1) or (i - 2 >= 0 and state[i - 2] != 'R'):
							newstate[i - 1] = 'L'
							newfalling.add(i - 1)

				if state[i] == 'R':
					if i + 1 < len(state) and state[i + 1] == '.':
						if (i == len(state) - 2) or (i + 2 < len(state) and state[i + 2] != 'L'):
							newstate[i + 1] = 'R'
							newfalling.add(i + 1)

			state = newstate
			falling = newfalling
	
		return ''.join(state[i] for i in range(len(state)))
