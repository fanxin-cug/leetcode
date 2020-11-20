class Solution {
public:
    int lengthOfLastWord(string s) {
        if(s.find(" ")!=-1){
            int index=s.find_last_of(" ");
            if(index==s.size()-1){
                s.erase(s.find_last_not_of(" ") + 1);
                index=s.find_last_of(" ");
                return s.size()-index-1;
            }else{
                return s.size()-index-1;
            }
        }else{
            if(s.empty()) return 0;
            else return s.size();
        }
    }
};