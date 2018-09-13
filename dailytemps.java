// https://leetcode.com/problems/daily-temps/description/

class Solution {
    public int[] dailyTemperatures(int[] temps) {
        int[] res = new int[temps.length];
        for (int i = 0; i < temps.length; i++) {
            int j = 0;
            do {
                j++;
            } while (i + j < temps.length && temps[i + j] <= temps[i]);
            if (i + j >= temps.length)
                res[i] = 0;
            else
                res[i] = j;
        }
        return res;        
    }
}
