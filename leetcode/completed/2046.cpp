#include <vector>

using namespace std;

class Solution {
public:
    bool checkAlmostEquivalent(string word1, string word2) {
        vector<int> counter(26, 0);

        for (int i = 0; i < word1.size(); i++) {
            counter[word1[i] - 'a']++;
            counter[word2[i] - 'a']--;
        }

        for (int i = 0; i < 26; i++) {
            if (abs(counter[i]) > 3) return false;
        }

        return true;

    }
};