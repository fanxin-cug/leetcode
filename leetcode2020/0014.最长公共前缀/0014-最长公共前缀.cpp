class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()) return string();
        sort(strs.begin(), strs.end());
        string start = strs.front(), end = strs.back();
        int i,num = min(start.size(), end.size());
        for(i = 0; i < num && start[i] == end[i]; i++);
        return start.substr(0,i);
    }
};