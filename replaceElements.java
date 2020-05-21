// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/ 

class Solution 
{
	public int[] replaceElements(int[] arr) 
	{
		int N = arr.length;
		int m = -1;
		int[] res = new int[N];

		res[N - 1] = -1;
        
		for (int i = N - 2; i >= 0; i--)
		{
			m = Math.max(m, arr[i + 1]);
			res[i] = m;
		}

		return res;
	}
}
