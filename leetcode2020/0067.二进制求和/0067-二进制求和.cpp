class Solution {
public:
    string addBinary(string a, string b) {
        int zero=abs(int(a.size())-int(b.size()));
        string fillzero(zero,'0');
        if(a.length()<b.length()){
            a=fillzero+a;
        }else{
            b=fillzero+b;
        }
        int carry=0;
        string res;
        for(int i=a.size()-1;i>=0;i--){
            int a1=a[i]-'0';
            int b1=b[i]-'0';
            int r=a1+b1+carry;
            carry=r/2;
            if(carry){
                res.push_back(r%2+'0');
            }else{
                res.push_back(r+'0');
            }
        }
        if(carry!=0) res.push_back(carry+'0');
        reverse(res.begin(),res.end());
        return res;
    }
};