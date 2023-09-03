public class 1054 {
    class Solution {
        public int[] rearrangeBarcodes(int[] barcodes) {
            HashMap<Integer, Integer> map = new HashMap<>();
            PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(pair -> -pair[0]));
    
            for (int code : barcodes) map.put(code, map.getOrDefault(code, 0) + 1);
    
            for (int key : map.keySet()) heap.add(new int[]{map.get(key), key});
    
            int[] res = new int[barcodes.length];
            int i = 0;
    
            while (!heap.isEmpty()) {
                int[] pair = heap.poll();
                int count = pair[0], num = pair[1];
                for (;count > 0; count--) {
                    if (i >= barcodes.length) i = 1;
                    res[i] = num;
                    i += 2;
                }
    
            }
    
            return res;
    
        }
    }
}
