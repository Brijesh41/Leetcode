class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in nums]
        dp[0] = nums[0]
        positive = False
        for i in range(1,len(nums)):
            if(nums[i]>0):
                positive = True
                break
        if(positive == False):
            return max(nums)
        else:
            sum = nums[0]
            for i in range(1,len(nums)):
                if(dp[i-1]<=0):
                    dp[i] = nums[i]
                    sum = max(sum,nums[i])
                else:
                    dp[i] = dp[i-1]+nums[i]
                    sum = max(sum,dp[i])
            return sum