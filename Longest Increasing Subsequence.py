class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        tails = []
        
        def binarysearch(i):
            
            l = 0
            r = len(tails)-1
            
            while(l<=r):
                m = int((l+r)/2)
                
                if(tails[m]<i):
                    l = m+1
                else:
                    r = m-1
            return l
        
        for i in nums:
            
            x = binarysearch(i)
            
            if(len(tails)>x):
                tails[x] = i
            else:
                tails.append(i)
            
            
        return len(tails)
        
        