class Solution {
public:
    bool isPalindrome(int x) {
        stringstream ss;
        string s,temp;
        ss<<x;
        ss>>s;
        temp=s;
        reverse(s.begin(),s.end());
        if(s==temp){
            return true;
        }else{
            return false;
        }
    }
};