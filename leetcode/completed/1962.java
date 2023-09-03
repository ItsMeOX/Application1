public class 1962 {
    class Solution {
        public int minStoneSum(int[] piles, int k) {
            PriorityQueue<Integer> pq = new PriorityQueue<>();
    
            for (int p : piles) {
                pq.add(-p);
            }
    
            for (; k > 0; k--) {
                int temp = -pq.poll();
                temp = temp - temp / 2;
                pq.add(-temp);
            }
    
            int res = 0;
            while (!pq.isEmpty()) {
                res -= pq.poll();
            }
    
            return res;
        }
    }
}
