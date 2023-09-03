public class 2154 {
    class Solution {
        public int findFinalValue(int[] nums, int original) {
            Arrays.sort(nums);
    
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == original) {
                    original <<= 1;
                }
            }
            
            return original;
    
        }
    }
    class Solution {
        public int findFinalValue(int[] nums, int original) {
            Set<Integer> set = new HashSet<>();
    
            for (int num : nums) {
                set.add(num);
            }
    
            while (set.contains(original)) {
                original *= 2;
            }
    
            return original;
    
        }
    }
}
