// https://leetcode.com/problems/palindrome-number

class Solution {
public:
    bool isPalindrome(int x) {
                  string a=to_string(x);
                  bool b=true;
                    for (int i = 0; i < int(a.size()/2); i++)
                    {
                        if (a[i]!=a[a.size()-1-i])
                        {
                            b=false;
                            break;
                        }

                    }
                    return b;
        
    } 
};