# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
	def subdomainVisits(self, cpdomains):
		count = {}
		for cp in cpdomains:
			n, dom = cp.split()
			n = int(n)
			dom = dom.split(".")

			sub = ""
			for d in dom[::-1]:
				if sub: 
					sub = d + "." + sub
				else:
					sub = d + sub

				if sub in count:
					count[sub] += n
				else:
					count[sub] = n

		return ["%d %s" % (count[sub], sub) for sub in count]
