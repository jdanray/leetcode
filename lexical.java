// https://leetcode.com/problems/lexicographical-numbers/

class Solution {
	public List<Integer> lexicalOrder(int n) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		order(0, n, result);
		return result;
	}

	public void order(int num, int n, ArrayList<Integer> result) {
		if (result.size() < n) {
			if (num > 0)
				result.add(num);
			int b = num * 10;
			for (int c = 0; c < 10; c++) {
				int newnum = b + c;
				if (newnum != 0 && newnum <= n)
					order(newnum, n, result);
			}
		}
	}
}
