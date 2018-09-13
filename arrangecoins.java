# https://leetcode.com/problems/arranging-coins/description/

class Solution {
    public int arrangeCoins(int n) {
        int k = 0;
        while (n - k > 0) {
            k++;
            n -= k;
        }
        return k;        
    }
}
