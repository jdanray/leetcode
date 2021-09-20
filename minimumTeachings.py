# https://leetcode.com/problems/minimum-number-of-people-to-teach/ 

class Solution(object):
	def minimumTeachings(self, n, languages, friendships):
		languages = [set(langs) for langs in languages]

		nonComms = []
		for (u, v) in friendships:
			if languages[u - 1] & languages[v - 1] == set():
				nonComms.append((u, v))

		res = float('inf')
		for lang in range(1, n + 1):
			users = set()
			for (u, v) in nonComms:
				if lang not in languages[u - 1]:
					users.add(u - 1)
				if lang not in languages[v - 1]:
					users.add(v - 1)

			res = min(res, len(users))

		return res
