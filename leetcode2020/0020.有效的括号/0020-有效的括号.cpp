class Solution {
public:
    bool isValid(string s) {
        if(s.empty()) return true;
        stack<char> st;
        st.push(s[0]);
        unordered_map<char,char> mp={{')','('},{']','['},{'}','{'}};
        unordered_map<char,char>::iterator it;
        for(int i=1;i<s.size();i++){
            it=mp.find(s[i]);
            if(it!=mp.end()&&!st.empty()&&it->second==st.top()){
                st.pop();
            }else{
                st.push(s[i]);
            }
        }
        if(st.empty()){
            return true;
        }else{
            return false;
        }
    }
};