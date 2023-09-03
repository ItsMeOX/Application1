public class 2070 {
    class Solution {
        private int bisect_right(int[][]items, int query) {
            int lo = 0, hi = items.length;
            while (lo < hi) {
                int m = lo + (hi - lo) / 2;
                if (items[m][0] > query) hi = m;
                else lo = m + 1;
            }
            return lo;
        }
    
        public int[] maximumBeauty(int[][] items, int[] queries) {
            int[] res = new int[queries.length];
            Arrays.fill(res, 0);
            Arrays.sort(items, (a, b) -> a[0] - b[0]);
            
            // update current max of every items[i][1]
            for (int i = 1; i < items.length; i++) {
                items[i][1] = Math.max(items[i][1], items[i-1][1]);
            }
    
            for (int i = 0; i < queries.length; i++) {
                int query = queries[i];
                if (query < items[0][0]) continue;
                int index = bisect_right(items, query);
                res[i] = items[index-1][1];
            }
    
            return res;
    
        }
    }
}
