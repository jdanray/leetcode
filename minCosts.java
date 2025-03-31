// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

class Solution {
	public int[] minCosts(int[] cost) {
		int m = Integer.MAX_VALUE;
		int[] res = new int[cost.length];
		for (int i = 0; i < cost.length; i++) {
			m = Math.min(m, cost[i]);
			res[i] = m;
		}
		return res;
	}
}