# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/ 

class Solution(object):
	def groupThePeople(self, groupSizes):
		N = len(groupSizes)
		people = sorted(range(N), key=lambda i: groupSizes[i])
		res = []
		i = 0
		while i < N:
			sz = groupSizes[people[i]]
			res.append([])
			while sz > 0:
				res[-1].append(people[i])
				sz -= 1
				i += 1
		return res

"""
After I solve a problem, I like to examine other people's solutions. I liked the following program:

vector<vector<int>> groupThePeople(vector<int>& gz) {
	vector<vector<int>> res, groups(gz.size() + 1);
	for (auto i = 0; i < gz.size(); ++i) {
		groups[gz[i]].push_back(i);
		if (groups[gz[i]].size() == gz[i]) {
			res.push_back({});
			swap(res.back(), groups[gz[i]]);
		}
	}
	return res;
}

Source: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/discuss/446534/C%2B%2BJava-Greedy

The above code is written in C++. Below I implement the algorithm in Python:
"""

class Solution(object):
	def groupThePeople(self, groupSizes):
		groups = collections.defaultdict(list)
		res = []
		for i, sz in enumerate(groupSizes):
			groups[sz].append(i) 
			if len(groups[sz]) == sz:
				res.append(groups[sz])
				groups[sz] = []
		return res
