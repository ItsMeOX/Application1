#include <string>
#include <iostream>

class Solution {
public:
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }

    bool halvesAreAlike(std::string s) {
        int left = 0;
        int right = 0;
        for(int i = 0; i < s.length()/2; i++) {
            if(isVowel(s[i])) left++;
            if(isVowel(s[s.length()-i-1])) right++;
        }
        return left == right;
    }
};