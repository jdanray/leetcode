# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution(object):
	def findDuplicate(self, paths):
		contents = collections.defaultdict(list)
		for path in paths:
			files = path.split()
			directory = files[0]
			files = files[1:]
            
			for f in files:
				cont = ''
				i = len(f) - 2
				while f[i] != '(':
					cont = f[i] + cont
					i -= 1
				name = f[:i]
				contents[cont].append(directory + '/' + name)
                
		return [contents[cont] for cont in contents if len(contents[cont]) >= 2]

"""
After I solve a problem, I like to study other people's solutions to the problem.

On this occasion, I discovered that someone had implemented the same idea, but in a more Pythonic and concise way. 

Source: https://leetcode.com/problems/find-duplicate-file-in-system/discuss/104122/Python-Straightforward-with-Explanation 
"""

class Solution(object):
	def findDuplicate(self, paths):
	M = collections.defaultdict(list)
	for line in paths:
		data = line.split()
		root = data[0]
		for file in data[1:]:
			name, _, content = file.partition('(')
			M[content[:-1]].append(root + '/' + name)

	return [x for x in M.values() if len(x) > 1]
