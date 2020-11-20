class Solution {
public:
    int reverse(int x) {
        stringstream ss;
        string s;
        ss<<x;
        ss>>s;
        if(x<0){
            string::iterator it=s.begin();
            it++;
            std::reverse(it,s.end());
        }else{
            std::reverse(s.begin(),s.end());
        }
        long res;
        ss.clear();
        ss<<s;
        ss>>res;
        if(res>INT_MIN&&res<INT_MAX){
            return int(res);
        }else{
            return 0;
        }
    }
};