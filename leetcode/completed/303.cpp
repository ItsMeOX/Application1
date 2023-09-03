#include <vector>

using namespace std;

class NumArray {
public:

    vector<int> prefix = {0};

    NumArray(vector<int>& nums) {
        for (int i = 1; i < nums.size()+1; i++) {
            prefix.push_back(prefix[i-1] + nums[i-1]);
        }
    }
    
    int sumRange(int left, int right) {
        return prefix[right+1] - prefix[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */