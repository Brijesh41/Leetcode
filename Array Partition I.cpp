class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int sum =0;
        int i =0;
        while(i+1<nums.size() ){
            // cout<<nums[i];
            sum+=min(nums[i],nums[i+1]);
            i+=2;
        }
        return sum;
    }
};