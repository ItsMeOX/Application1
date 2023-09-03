// XOR is reversible, 
// res of range of XOR from i to j = XOR(i ~ j) ^ XOR(0 ~ i-1).

public class 1310 {
    class Solution {
        public int[] xorQueries(int[] arr, int[][] queries) {
            int[] prefix = new int[arr.length];
            prefix[0] = arr[0];
    
            for (int i = 1; i < arr.length; i++) {
                prefix[i] = arr[i] ^ prefix[i-1];
            }
    
            int[] res = new int[queries.length];
            for (int i = 0; i < queries.length; i++) {
                int[] query = queries[i];
                int s = query[0], e = query[1];
    
                res[i] = s == 0 ? prefix[e] : prefix[e] ^ prefix[s-1];
            }
    
            return res;
    
        }
    }
}
