# https://leetcode.com/problems/invalid-transactions/

class Solution(object):
	def invalidTransactions(self, transactions):
		struct = set()
		hist = collections.defaultdict(set)
		for idx, trans in enumerate(transactions):
			name, time, amount, city = trans.split(',')
			time, amount = int(time), int(amount)
			struct.add((idx, name, time, amount, city))
			hist[name].add((idx, time, city))

		res = set()
		for (idx, name, time, amount, city) in struct:
			if amount > 1000:
				res.add(transactions[idx])

			for (hidx, htime, hcity) in hist[name]:
				if abs(time - htime) <= 60 and city != hcity:
					res.add(transactions[idx])
					res.add(transactions[hidx])

		return list(res)
