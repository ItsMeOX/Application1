#include <string>

using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        int counter[26] = {0};
        char max_char;
        int max_freq = 0;
        int n = s.size();

        for (auto& c : s) {
            counter[c - 'a']++;
            if (counter[c - 'a'] > max_freq) {
                max_char = c;
                max_freq = counter[c - 'a'];
            }
        }

        if (max_freq > (n + 1)/2) return "";

        int i = 0;

        while(max_freq-- > 0) {
            s[i] = max_char;
            i += 2;
        }
        counter[max_char - 'a'] = 0;

        for (int j = 0; j < 26; j++) {
            while (counter[j]-- > 0) {
                if (i >= n) i = 1;
                s[i] = 'a' + j;
                i += 2;
            }
        }

        return s;

    }
};