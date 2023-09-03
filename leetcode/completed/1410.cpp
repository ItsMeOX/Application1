#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    string entityParser(string text) {
        unordered_map<string, string> mapper = {
            {"&quot;", "\""},
            {"&apos;", "'"},
            {"&gt;", ">"},
            {"&lt;", "<"},
            {"&frasl;", "/"},
            {"&amp;", "&"},
        };

        string res = "";
        string temp = "";

        for (int i = 0; i < text.length(); i++) {
            if (text[i] == '&') {
                res += temp;
                temp = '&';
            }
            else if (text[i] == ';') {
                temp += text[i];   
                if (mapper.find(temp) != mapper.end()) {
                    res += mapper[temp];
                    temp = "";
                }
                else {
                    res += temp;
                    temp = "";
                }
            } 
            else {
                temp += text[i];
            }
        }

        res += temp;

        return res;
    }
};
