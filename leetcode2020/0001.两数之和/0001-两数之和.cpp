class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        int size=nums.size();
        unordered_map<int,int> hash;
        for(int i=0;i<size;i++){
            hash.insert(make_pair(nums[i],i));
        }
        for(int i=0;i<size;i++){
            int v=target-nums[i];
            //unordered_map<int,int>::iterator it=hash.find(v);
            auto it=hash.find(v);
            if(it!=hash.end()&&it->second!=i){
                res.push_back(i);
                res.push_back(it->second);
                return res;
            }
        }
        return res;
    }
};