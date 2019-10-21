# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution(object):
	def removeSubfolders(self, folder):
		folder = sorted(folder, key=len)
		res = []
		seen = set()
		for fold in folder:
			isoutput = True
			name = ""
			for f in fold:
				if f == '/' and name in seen:
					isoutput = False
					break
				name += f
                    
			if isoutput:
				res.append(fold)
                
			seen.add(fold)
            
		return res
