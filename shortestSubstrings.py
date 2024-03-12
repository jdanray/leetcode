# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/ 

class Solution(object):
	def shortestSubstrings(self, arr):
		# count all substrings for all arr[i]
		count = collections.Counter()
		for s in arr:
			for i in range(len(s)):
				sub = ''
				for j in range(i, len(s)):
					sub += s[j]
					count[sub] += 1

		res = ['' for _ in range(len(arr))]
		for i, s in enumerate(arr):
			# remove substrings for arr[i]
			for j in range(len(s)):
				sub = ''
				for k in range(j, len(s)):
					sub += s[k]
					count[sub] -= 1

			# find shortest uncommon substring in arr[i]
			cand = ''
			for j in range(len(s)):
				sub = ''
				for k in range(j, len(s)):
					sub += s[k]
					if count[sub] == 0 and (cand == '' or len(sub) < len(cand) or (len(sub) == len(cand) and sub < cand)):
						cand = sub
			res[i] = cand

			# re-add substrings for arr[i] 
			for j in range(len(s)):
				sub = ''
				for k in range(j, len(s)):
					sub += s[k]
					count[sub] += 1

		return res
